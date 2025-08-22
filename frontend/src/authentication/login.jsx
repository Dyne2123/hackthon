import { useState } from "react";

const studentLoginUrl = "http://127.0.0.1:5000/student_login";
const staffLoginUrl = "http://127.0.0.1:5000/staff_login";

export default function Login() {
  const [selected, setSelected] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [staffId, setStaffId] = useState("");
  const [staffPassword, setStaffPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (selected === "student") {
      fetch(studentLoginUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          password: password,
          role: "student",
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Server response:", data);
          
        })
        .catch((error) => console.error(error));
    } else if (selected === "staff") {
      // Staff login
      fetch(staffLoginUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          staffId: staffId,
          password: staffPassword,
          role: "staff",
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Server response:", data);
          
        })
        .catch((error) => console.error(error));
    } else {
      console.log("Please select a role");
    }
  };

  return (
    <div>
      <h1>Login Page</h1>
      <form onSubmit={handleSubmit}>
        <select value={selected} onChange={(e) => setSelected(e.target.value)}>
          <option value="">-- Select Role --</option>
          <option value="student">Student</option>
          <option value="staff">Staff</option>
        </select>

        {selected === "student" && (
          <div>
            <h2>Student Login</h2>
            <input
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />{" "}
            <br />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />{" "}
            <br />
          </div>
        )}

        {selected === "staff" && (
          <div>
            <h2>Staff Login</h2>
            <input
              type="text"
              placeholder="Staff ID"
              value={staffId}
              onChange={(e) => setStaffId(e.target.value)}
            />{" "}
            <br />
            <input
              type="password"
              placeholder="Password"
              value={staffPassword}
              onChange={(e) => setStaffPassword(e.target.value)}
            />{" "}
            <br />
          </div>
        )}

        <button type="submit">Login</button>
      </form>
    </div>
  );
}
