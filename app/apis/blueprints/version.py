from flask import Blueprint
from flask_restplus import Api
from app.apis.namespaces.version.endpoints import api as version


blueprint = Blueprint("version", __name__, url_prefix="/api")

api = Api(
    blueprint,
    title="Resources management API",
    version="1.0",
    description="CRUD on resources",
)

api.add_namespace(version)
