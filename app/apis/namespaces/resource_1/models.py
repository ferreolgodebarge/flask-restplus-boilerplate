from flask_restplus import fields


resource_1 = {
    "uuid": fields.String(
        required=True,
        description="Resource 1 identifier",
    ),
    "name": fields.String(
        required=True,
        description="Resource 1 name",
    ),
    "description": fields.String(
        required=False,
        description="Resource 1 description",
    ),
}

resource_1_request = {
    "name": fields.String(
        required=True,
        description="Resource 1 name",
    ),
    "description": fields.String(
        required=False,
        description="Resource 1 description",
    ),
}
