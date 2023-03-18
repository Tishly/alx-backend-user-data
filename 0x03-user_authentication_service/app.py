#!/usr/bin/env python3

from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> str:
    """Base route for API
    """
    return jsonify({"meassage": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users(email: str, password: str) -> str:
    """Route to register new users
    Return: JSON
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    message = {"email": email, "message": "user created"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
