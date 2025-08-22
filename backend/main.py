from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt  
import os
from database import register_users_student,login_student,register_users_staff,login_staff

app = Flask(__name__)
CORS(app)
load_dotenv()

auth_secret = os.getenv("AUTH_SECRET")


class Authentication:
    def __init__(self, auth_secret):
        self.auth_secret = auth_secret

    def createAuthToken(self, userId):
        payload = {
            "userId": userId,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=500)
        }
        token = jwt.encode(payload, self.auth_secret, algorithm="HS256")
       
        if isinstance(token, bytes):
            token = token.decode("utf-8")
        return token

    def decodeToken(self, token):
        try:
            payload = jwt.decode(token, self.auth_secret, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}
        except Exception as e:
            return {"error": str(e)}


auth = Authentication(auth_secret)


@app.route('/student_register', methods=['POST'])
def student_register():
    response = request.get_json()
    username = response.get("studentUserName")
    password = response.get("studentPassword")
    
    print(username,password)
    
    register_status = register_users_student(username, password)

    if register_status == "1":
        
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})
    
@app.route('/student_login',methods = ['POST'])
def student_login():
    response = request.get_json()
    username = response.get("username")
    password = response.get("password")
    role = response.get("role")
    auth = login_student(username,password,role)
    if auth == "1":
        return jsonify({"status":"success"})
    else:
        return jsonify({"status":"failed"})
    

@app.route('/staff_register', methods=['POST'])
def staff_register():
    response = request.get_json()
    username = response.get("staffUserName")
    password = response.get("staffPassword")
    
    print(username,password)
    
    register_status = register_users_staff(username, password)

    if register_status == "1":
        
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})
    
@app.route('/student_login',methods = ['POST'])
def staff_login():
    response = request.get_json()
    username = response.get("username")
    password = response.get("password")
    role = response.get("role")
    auth = login_staff(username,password,role)
    if auth == "1":
        return jsonify({"status":"success"})
    else:
        return jsonify({"status":"failed"})



# @app.route('/staff_register', methods=['POST'])
# def staff_register():
#     response = request.get_json()
#     staffId = response.get("staffId")
#     password = response.get("staffPassword")
#     role = "staff"

#     random_id = generate_unique_key()
#     register_status = register_users(None, password, role, staffId, random_id)

#     if register_status == "1":
#         token = auth.createAuthToken(random_id)
#         return jsonify({"status": "success", "token": token})
#     else:
#         return jsonify({"status": "failed"})
    
# @app.route('/student_login', methods=['POST'])
# def student_login():
#     response = request.get_json()
#     username = response.get("username")
#     password = response.get("password")

#     # 🔹 Validate user credentials (dummy check for now)
#     # Replace with DB validation
#     if username == "student1" and password == "pass123":
#         # generate JWT for this student
#         random_id = generate_unique_key()
#         token = auth.createAuthToken(random_id)
#         return jsonify({"status": "success", "token": token})
#     else:
#         return jsonify({"status": "failed", "message": "Invalid credentials"}), 401


# @app.route('/staff_login',methods=['POST'])
# def staff_login():
#     pass



if __name__ == "__main__":
    app.run(debug=True)