from flask_restplus import Namespace, Resource
from app.apis.namespaces.resourceOne.models import (
    resourceOne,
    resourceOne_request,
)
from app.core.resources.resourceOne import (
    list_resourceOne as list_resource,
    create_resourceOne as create_resource,
    read_resourceOne as read_resource,
    update_resourceOne as update_resource,
    delete_resourceOne as delete_reseource,
)

api = Namespace(
    'resourceOne',
    description='CRUD on resourceOne',
)

resource_model = api.model("resourceOne", resourceOne)
resource_request_model = api.model("resourceOne request", resourceOne_request)


@api.route("")
class ResourceOneList(Resource):
    @api.doc("list_resourceOne")
    @api.response(code=200, model=[resource_model], description="Success")
    def get(self):
        """List resourceOne"""
        return list_resource(), 200

    @api.doc("create_resourceOne")
    @api.expect(resource_request_model)
    @api.response(code=201, model=resource_model, description="Success")
    def post(self):
        """Create a new resourceOne"""
        name = api.payload['name']
        description = api.payload['description']
        return create_resource(name, description), 201


@api.route("/<uuid:uuid>")
class ResourceOne(Resource):
    @api.doc("read_resourceOne")
    @api.response(code=200, model=resource_model, description="Success")
    def get(self, uuid):
        """Get a resourceOne by uuid"""
        return read_resource(uuid), 200

    @api.doc("update_resourceOne")
    @api.response(code=200, model=resource_model, description="Success")
    def put(self, uuid, name, description=""):
        """Update a resourceOne by uuid"""
        return update_resource(uuid, name, description), 200

    @api.doc("delete_resourceOne")
    @api.response(code=204, description="Deleted")
    def delete(self, uuid):
        """Delete a resourceOne by uuid"""
        return delete_reseource(uuid), 204
