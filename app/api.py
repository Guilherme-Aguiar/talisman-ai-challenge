from flask_restful import Api
from app.controller import ParsePDFAndRunPrompt
from app.errors import errors

# Flask API Configuration
api = Api(
    catch_all_404s=True,
)

api.add_resource(ParsePDFAndRunPrompt, '/answer')