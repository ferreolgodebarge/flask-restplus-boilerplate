from flask import Blueprint
from flask_restplus import Api
from application.apis.namespaces.version.endpoints import api as version


blueprint = Blueprint("version", __name__, url_prefix="/api")

api = Api(
    blueprint,
    title="Resources management API",
    version="1.0",
    description="CRUD on resources",
    validate=True,
)

api.add_namespace(version)
