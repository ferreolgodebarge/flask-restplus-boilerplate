from flask_restplus import fields


resourceOne = {
    "uuid": fields.String(
        required=True,
        description="resourceOne identifier",
    ),
    "name": fields.String(
        required=True,
        description="resourceOne name",
    ),
    "description": fields.String(
        required=False,
        description="resourceOne description",
    ),
}

resourceOne_request = {
    "name": fields.String(
        required=True,
        description="resourceOne name",
    ),
    "description": fields.String(
        required=False,
        description="resourceOne description",
    ),
}
