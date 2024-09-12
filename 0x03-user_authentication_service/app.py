#!/usr/bin/env python3
"""
A basic Flask App"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def index() -> str:
    """GET route that returns a JSON response."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """_summary_
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # regsiter user if user does not exist
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """"
    Login functionality"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not (AUTH.valid_login(email, password)):
        abort(401)
    else:
        # Create a session
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)

    return response

@app.route('/sessions', method=['DELETE'])
def logout() -> str:
    """
    Logout functionality"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
