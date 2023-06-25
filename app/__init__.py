from flask import Flask, jsonify, json
from flask_restful import Resource, Api
from app.api import api
from app.config import config_by_name
from app.controller import ParsePDFAndRunPrompt

from flask_swagger_ui import get_swaggerui_blueprint

def create_app(config_name='dev'):
    app = Flask(__name__)
    # Sets file upload limit 16MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

    class HealthCheck(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HealthCheck, '/')

    app.config.from_object(config_by_name[config_name])

    # Flask API Initialization
    api.init_app(app)   

    # Configure Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = 'http://localhost:5000/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Sample API"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/swagger.json')
    def swagger():
        with open('swagger.json', 'r') as f:
            return jsonify(json.load(f))

    return app
