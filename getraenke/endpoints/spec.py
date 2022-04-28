from flask import jsonify
from flask import current_app as app
from flask.views import MethodView
from flask_swagger import swagger

class SpecApi(MethodView):
    """ /spec """

    def get(self):
        """
        Returns Swagger specification for this project
        This project is documented using docstrings. These docstrings can be parsed using flask_swagger, whose output will be returned by this endpoint in a json-ified form.
        ---
        tags:
            - documentation
        responses:
            200:
                description: Returns jsonified Swagger specification
        """

        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "API des digitalen Getraenkeverkaufs"

        swag['tags'] = [
            {
                'name': 'documentation',
                'description': 'Swagger specification endpoint.'
            }
        ];

        return jsonify(swag)
