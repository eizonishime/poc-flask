from flask import Flask, request, make_response, Blueprint
import os
from routes.root import root


app = Flask(__name__, static_url_path='',
            static_folder='public')
not_authenticated = Blueprint('not_authenticated', __name__)


@not_authenticated.route('/healthcheck', methods=['GET'])
def healthcheck():
    return make_response('ok', 200)


app.register_blueprint(not_authenticated)
app.register_blueprint(root)

if __name__ == "__main__":
    app.run()

