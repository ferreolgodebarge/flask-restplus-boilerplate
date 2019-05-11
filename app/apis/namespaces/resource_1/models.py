from flask_restplus import fields


resource_1 = {
    "uuid": fields.String(
        required=True,
        description="resource_1 identifier",
    ),
    "name": fields.String(
        required=True,
        description="resource_1 name",
    ),
    "description": fields.String(
        required=False,
        description="resource_1 description",
    ),
}

resource_1_request = {
    "name": fields.String(
        required=True,
        description="resource_1 name",
    ),
    "description": fields.String(
        required=False,
        description="resource_1 description",
    ),
}
