import uuid as random
from ...models.resource_1 import (
        db,
        Resource_1,
)
from ..exceptions.generic import (
    BackendIssue,
    ConflictError,
    ResourceNotFound,
)


def list_resource_1():
    try:
        resources = Resource_1.query.all()
        response = []
        for resource in resources:
            response.append(resource.to_dict())
        return response
    except Exception:
        message = "Unable to contact backend"
        raise BackendIssue(message)


def create_resource_1(name, description):
    try:
        resource = Resource_1.query.filter_by(name=name).first()
        if not resource:
            uuid = str(random.uuid4())
            response = Resource_1(
                uuid=uuid, name=name, description=description)
            db.session.add(response)
            db.session.commit()
            return response.to_dict()
        else:
            message = "A resource already exists with this name: {}".format(
                name)
            raise ConflictError(message)
    except ConflictError as e:
        raise e
    except Exception:
        message = "Unable to contact backend"
        raise BackendIssue(message)


def read_resource_1(uuid):
    try:
        resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
        if resource:
            return resource.to_dict()
        else:
            message = "Resource {} not found".format(str(uuid))
            raise ResourceNotFound(message)
    except ResourceNotFound as e:
        raise e
    except Exception:
        message = "Unable to contact backend"
        raise BackendIssue(message)


def update_resource_1(uuid, name, description):
    try:
        resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
        if resource:
            resource.name = name
            resource.description = description
            db.session.commit()
            return resource.to_dict()
        else:
            message = "Resource {} not found".format(str(uuid))
            raise ResourceNotFound(message)
    except ResourceNotFound as e:
        raise e
    except Exception:
        message = "Unable to contact backend"
        raise BackendIssue(message)


def delete_resource_1(uuid):
    try:
        resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
        if resource:
            Resource_1.query.filter_by(uuid=str(uuid)).delete()
            db.session.commit()
        else:
            message = "Resource {} not found".format(str(uuid))
            raise ResourceNotFound(message)
    except ResourceNotFound as e:
        raise e
    except Exception:
        message = "Unable to contact backend"
        raise BackendIssue(message)