from flask import Blueprint
from flask_restplus import Api
from app.apis.namespaces.resourceOne.endpoints import api as resourceOne


blueprint = Blueprint("v1", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    title="Resources management API",
    version="1.0",
    description="CRUD on resources",
)

api.add_namespace(resourceOne)
