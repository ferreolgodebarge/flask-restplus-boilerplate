from flask_restplus import Namespace, Resource
from app.apis.namespaces.resource_1.models import (
    resource_1,
    resource_1_request,
)
from app.core.resources.resource_1 import (
    list_resource_1 as list_resource,
    create_resource_1 as create_resource,
    read_resource_1 as read_resource,
    update_resource_1 as update_resource,
    delete_resource_1 as delete_reseource,
)

api = Namespace(
    'resource-1',
    description='CRUD on resource-1',
)

resource_model = api.model("resource_1", resource_1)
resource_request_model = api.model("resource_1 request", resource_1_request)


@api.route("")
class Resource_1_List(Resource):
    @api.doc("list_resource_1")
    @api.response(code=200, model=[resource_model], description="Success")
    def get(self):
        """List resource-1"""
        return list_resource(), 200

    @api.doc("create_resource_1")
    @api.expect(resource_request_model)
    @api.response(code=201, model=resource_model, description="Success")
    def post(self):
        """Create a new resource-1"""
        name = api.payload['name']
        description = api.payload['description']
        return create_resource(name, description), 201


@api.route("/<uuid:uuid>")
class Resource_1(Resource):
    @api.doc("read_resource_1")
    @api.response(code=200, model=resource_model, description="Success")
    def get(self, uuid):
        """Get a resource-1 by uuid"""
        return read_resource(uuid), 200

    @api.doc("update_resource_1")
    @api.expect(resource_request_model)
    @api.response(code=200, model=resource_model, description="Success")
    def put(self, uuid):
        """Update a resource-1 by uuid"""
        name = api.payload['name']
        description = api.payload['description']
        return update_resource(uuid, name, description), 200

    @api.doc("delete_resource_1")
    @api.response(code=204, description="Deleted")
    def delete(self, uuid):
        """Delete a resource-1 by uuid"""
        return delete_reseource(uuid), 204
