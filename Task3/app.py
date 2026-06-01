# TASK 3: Secure Coding Review
# ● Select a programming language and application to audit.
# ● Perform a code review to identify security vulnerabilities.
# ● Use tools like static analyzers or manual inspection methods.
# ● Provide recommendations and best practices for secure coding.
# ● Document findings and suggest remediation steps for safer code.

# first install  (python -m pip install bandit)
# In Last first run app.py then open new terminal and run (python -m bandit -r .)

# in MongoDB ( use secure_review ,  db.users.find())

from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["secure_review"]
users = db["users"]


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    # Vulnerable Login
    user = users.find_one({"username": username, "password": password})

    if user:
        return "Login Successful"

    return "Invalid Login"


if __name__ == "__main__":
    app.run(debug=False)
