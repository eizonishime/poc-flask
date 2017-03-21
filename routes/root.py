from flask import request, jsonify, Blueprint

root = Blueprint('root', __name__)

@root.route("/")
def main():
    return ""