from flask import Flask
from flask_cors import CORS

from getraenke.endpoints.spec import SpecApi

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.add_url_rule("/spec", view_func=SpecApi.as_view("spec_api"))

    return app
