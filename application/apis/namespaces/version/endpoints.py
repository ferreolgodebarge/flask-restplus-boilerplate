from flask_restplus import Namespace, Resource, fields


api = Namespace(
    'version',
    description='Display available API versions',
)

available_version = api.model(
    "Available version",
    {
        "version": fields.String(
            required=True,
            description="Discplay API version",
        ),
        "documentation": fields.String(
            required=True,
            description="Display API version documentation URL",
        ),
    }
)

version_model = api.model(
    "Version",
    {
        "available_versions": fields.Nested(
            model=available_version,
            description="Display all API available versions",
            as_list=True,
        ),
        "package_version": fields.String(
            required=True,
            description="Display applicative package version",
        ),
        "hostname": fields.String(
            required=True,
            description="Display hostname",
        ),
    },
)


@api.route("")
class Version(Resource):
    @api.doc('get_version')
    @api.response(code=200, model=version_model, description='Success')
    def get(self):
        return "not yet implemented", 200
