from flask import jsonify
from flask import current_app as app
from flask.views import MethodView
from flask_swagger import swagger

class SpecApi(MethodView):
    """ /spec """

    def get(self):
        """
        Returns Swagger specification for this project
        ---
        tags:
            - documentation
        respsonses:
            200:
                description: Returns jsonified specification
        """

        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "API des digitalen Getraenkeverkaufs"

        return jsonify(swag)
