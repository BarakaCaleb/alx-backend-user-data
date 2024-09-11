#!/usr/bin/env python3
"""
A basic Flask App"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """GET route that returns a JSON response."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
