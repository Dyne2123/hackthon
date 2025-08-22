import { useState } from "react";
const url = "http://127.0.0.1:5000/student_register"
const url2 = "http://127.0.0.1:5000/staff_register"
export default function Register() {
  const [selected, setSelected] = useState("");
  

 
  const [studentId, setStudentId] = useState("");
  const [studentUsername, setStudentUsername] = useState("");
  const [studentPassword, setStudentPassword] = useState("");
  const [staffId, setStaffId] = useState("");
  const [staffPassword, setStaffPassword] = useState("");

  
  const handleSubmit = (e) => {
    e.preventDefault();
    //student data
    if (selected === "student") {
    
      console.log("Student Data:", {
        studentId,
        studentUsername,
        studentPassword,
      });
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({"studentUserName":studentUsername,"studentPassword":studentPassword,"studentId":studentId,"role":"student"})
            })
            .then(response => response.json())
            .then(data => {
                console.log("Server response: ",data);
            }).catch(error => {
                console.error(error);

        })
    } else if (selected === "staff") {
        //staff register
      console.log("Staff Data:", {
        staffId,
        staffPassword,
      });

      fetch(url2,{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({"staffId":staffId,"staffPassword":staffPassword})
            })
            .then(response => response.json())
            .then(data => {
                console.log("Server response: ",data);
            }).catch(error => {
                console.error(error);

        })
    } else {
      console.log("Please select role");
    }
  };

  return (
    <div>
      <h1>Register page</h1>

      <form onSubmit={handleSubmit}>
        <select value={selected} onChange={(e) => setSelected(e.target.value)}>
          <option value="">-- Select --</option>
          <option value="student">Student</option>
          <option value="staff">Staff</option>
        </select>

        {selected === "student" && (
          <div>
            <h2>Student Registration</h2>
            <input
              type="text"
              placeholder="Student ID"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
            />{" "}
            <br />
            <input
              type="text"
              placeholder="Username"
              value={studentUsername}
              onChange={(e) => setStudentUsername(e.target.value)}
            />{" "}
            <br />
            <input
              type="password"
              placeholder="Password"
              value={studentPassword}
              onChange={(e) => setStudentPassword(e.target.value)}
            />{" "}
            <br />
          </div>
        )}

        {selected === "staff" && (
          <div>
            <h2>Staff Registration</h2>
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

        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
