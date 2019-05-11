import uuid as random
from app.models.resource_1 import (
    db,
    Resource_1,
)


def list_resource_1():
    resources = Resource_1.query.all()
    response = []
    for resource in resources:
        response.append(resource.to_dict())
    return response


def create_resource_1(name, description):
    resource = Resource_1.query.filter_by(name=name).first()
    if not resource:
        uuid = str(random.uuid4())
        response = Resource_1(uuid=uuid, name=name, description=description)
        db.session.add(response)
        db.session.commit()
        return response.to_dict()


def read_resource_1(uuid):
    resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
    if resource:
        return resource.to_dict()


def update_resource_1(uuid, name, description):
    resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
    if resource:
        resource.name = name
        resource.description = description
        db.session.commit()
        return resource.to_dict()


def delete_resource_1(uuid):
    resource = Resource_1.query.filter_by(uuid=str(uuid)).first()
    if resource:
        Resource_1.query.filter_by(uuid=str(uuid)).delete()
        db.session.commit()
        return 0
