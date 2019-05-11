import uuid as random
from app.models.resourceOne import (
    db,
    ResourceOne,
)


def list_resourceOne():
    resources = ResourceOne.query.all()
    response = []
    for resource in resources:
        response.append(resource.to_dict())
    return response


def create_resourceOne(name, description):
    resource = ResourceOne.query.filter_by(name=name).first()
    if not resource:
        uuid = str(random.uuid4())
        response = ResourceOne(uuid=uuid, name=name, description=description)
        db.session.add(response)
        db.session.commit()
        return response.to_dict()


def read_resourceOne(uuid):
    resource = ResourceOne.query.filter_by(uuid=str(uuid)).first()
    if resource:
        return resource.to_dict()


def update_resourceOne(uuid, name, description):
    resource = ResourceOne.query.filter_by(uuid=str(uuid)).first()
    if resource:
        resource.name = name
        resource.description = description
        db.session.commit()
        return resource.to_dict()


def delete_resourceOne(uuid):
    resource = ResourceOne.query.filter_by(uuid=str(uuid)).first()
    if resource:
        ResourceOne.query.filter_by(uuid=uuid).delete()
        db.session.commit()
        return 0
