from flask_restplus import Namespace, Resource
from .models import (
    resource_1,
    resource_1_request,
    error,
)
from ....core.resources.resource_1 import (
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
error_model = api.model("error", error)


@api.route("")
class Resource_1_List(Resource):
    @api.doc("list_resource_1")
    @api.response(code=200, model=[resource_model], description="Success")
    @api.response(code=503, model=error_model, description="Backend issue")
    def get(self):
        """List resource-1"""
        try:
            return list_resource(), 200
        except Exception as e:
            return e.to_dict(), e.status_code

    @api.doc("create_resource_1")
    @api.expect(resource_request_model)
    @api.response(code=201, model=resource_model, description="Success")
    @api.response(code=409, model=error_model, description="Name conflict")
    @api.response(code=503, model=error_model, description="Backend issue")
    def post(self):
        """Create a new resource-1"""
        try:
            name = api.payload['name']
            description = api.payload['description']
            return create_resource(name, description), 201
        except Exception as e:
            return e.to_dict(), e.status_code


@api.route("/<uuid>")
class Resource_1(Resource):
    @api.doc("read_resource_1")
    @api.response(code=200, model=resource_model, description="Success")
    @api.response(
        code=404,
        model=error_model,
        description="Resource not found",
    )
    @api.response(code=503, model=error_model, description="Backend issue")
    def get(self, uuid):
        """Get a resource-1 by uuid"""
        try:
            return read_resource(uuid), 200
        except Exception as e:
            print("hello")
            return e.to_dict(), e.status_code

    @api.doc("update_resource_1")
    @api.expect(resource_request_model)
    @api.response(code=200, model=resource_model, description="Success")
    @api.response(
        code=404,
        model=error_model,
        description="Resource not found",
    )
    @api.response(code=503, model=error_model, description="Backend issue")
    def put(self, uuid):
        """Update a resource-1 by uuid"""
        try:
            name = api.payload['name']
            description = api.payload['description']
            return update_resource(uuid, name, description), 200
        except Exception as e:
            return e.to_dict(), e.status_code

    @api.doc("delete_resource_1")
    @api.response(code=204, description="Deleted")
    @api.response(
        code=404,
        model=error_model,
        description="Resource not found",
    )
    @api.response(code=503, model=error_model, description="Backend issue")
    def delete(self, uuid):
        """Delete a resource-1 by uuid"""
        try:
            delete_reseource(uuid)
            return '', 204
        except Exception as e:
            return e.to_dict(), e.status_code
