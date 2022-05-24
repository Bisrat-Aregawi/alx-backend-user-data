#!/usr/bin/env python3
"""Module defines a flask application"""
from typing import Tuple
from flask.wrappers import Response
from werkzeug.wrappers import Response
from auth import Auth
from flask import abort, Flask, redirect, request 
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


@app.route("/sessions", methods=["POST"])
def login() -> Tuple[Response, int]:
    """
    Handle login post request
    """
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    if AUTH.valid_login(email, password) is True:
        cookie = AUTH.create_session(email)
        if cookie:
            out = jsonify(
                {
                    "email": "{}".format(email),
                    "message": "logged in"
                }
            )
            out.set_cookie("session_id", cookie)
            return (out, 200)
    abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> Response:
    """Destory the current user session and redirect to home"""
    sessid = request.cookies.get("session_id")
    if sessid:
        usr = AUTH._db.find_user_by(session_id=sessid)
        if usr:
            AUTH.destroy_session(int(usr.id))
            return redirect("/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
