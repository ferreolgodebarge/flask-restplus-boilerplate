def init_app(app):
    from . import resource_1
    from ..tools import db
    # Create tables
    db.create_all(app=app)
    print(" * Data tables initialized : {}".format(
        resource_1.Resource_1.resource_name,
    ))
