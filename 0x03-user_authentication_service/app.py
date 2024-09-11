#!/usr/bin/env python3
"""
A basic Flask App"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)

AUTH = Auth()

@app.route("/", methods=["GET"])
def index() -> str:
    """GET route that returns a JSON response."""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users() -> str:
    """POST route that returns a JSON response."""
    password = request.form.get("password")
    email = request.form.get("email")
    # Register user if doesnt exist
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"email": email, "message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
