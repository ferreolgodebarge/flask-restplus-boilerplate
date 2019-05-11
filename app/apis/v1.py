from flask import Blueprint
from flask_restplus import Api
from app.apis.namespaces.resource_1.endpoints import api as resource_1


blueprint = Blueprint("v1", __name__, url_prefix="/api/v1")

api = Api(
    blueprint,
    title="Resources management API",
    version="1.0",
    description="CRUD on resources",
)

api.add_namespace(resource_1)