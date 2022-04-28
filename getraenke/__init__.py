from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from getraenke.database import get_database

from getraenke.endpoints.spec import SpecApi

def create_app(config=None):
    # Load .env file
    load_dotenv()

    # Create Flask app and enable CORS
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Add all controllers to app
    app.add_url_rule("/spec", view_func=SpecApi.as_view("spec_api"))

    @app.cli.command("init-db")
    def init_db():
        """
        Initializes schema in database specified in .env file.
        """
        print ("Trying to create tables")
        from getraenke.models.product import Product

        get_database().create_tables([Product])
        print ("Finished creating tables")

    return app
