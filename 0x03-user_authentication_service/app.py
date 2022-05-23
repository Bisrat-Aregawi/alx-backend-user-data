#!/usr/bin/env python3
"""Module defines a flask application"""
from typing import Tuple
from flask.wrappers import Response
from auth import Auth
from flask import Flask, request
from flask.json import jsonify


# Instantiate a WSGI application
app = Flask(__name__)

# Instantiate an Auth object
AUTH = Auth()


@app.route('/', methods=["GET"])
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register() -> Tuple[Response, int]:
    """
    Register a new user using passed form data fields
    """
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    try:
        AUTH.register_user(email, password)
        return (
            jsonify({
                "email": "{}".format(email),
                "message": "user created"
            }),
            200
        )
    except ValueError:
        return (
            jsonify({
                "message": "email already registered"
            }),
            400
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
