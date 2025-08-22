from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt   # ✅ this works correctly once PyJWT is installed
import os
from database import generate_unique_key, register_users

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
        # PyJWT >= 2.x returns a str, older versions return bytes
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
    studentId = response.get("studentId")
    role = response.get("role")

    random_id = generate_unique_key()
    register_status = register_users(username, password, role, studentId, random_id)

    if register_status == "1":
        token = auth.createAuthToken(random_id)
        return jsonify({"status": "success", "token": token})
    else:
        return jsonify({"status": "failed"}), 400


@app.route('/staff_register', methods=['POST'])
def staff_register():
    response = request.get_json()
    staffId = response.get("staffId")
    password = response.get("staffPassword")
    role = "staff"

    random_id = generate_unique_key()
    register_status = register_users(None, password, role, staffId, random_id)

    if register_status == "1":
        token = auth.createAuthToken(random_id)
        return jsonify({"status": "success", "token": token})
    else:
        return jsonify({"status": "failed"}), 400


if __name__ == "__main__":
    app.run(debug=True)