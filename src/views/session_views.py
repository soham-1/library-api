from flask import Blueprint, current_app, Response, session

session_bp = Blueprint("session_view", __name__)

@session_bp.route('/', methods=["GET"])
def index():
    session['self_name'] = "hello"
    return Response("session set")

@session_bp.route('/get', methods=["GET"])
def get_name():
    return Response(session.get("self_name", None))

@session_bp.route('/delete', methods=["GET"])
def delete_name():
    session.pop("self_name", None)
    print(session.get("self_name"))
    return Response(session.get("self_name", None))