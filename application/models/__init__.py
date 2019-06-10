def init_app(app):
    """[Models initializer]

    Arguments:
        app {[Flask]} -- [Flask application]
    """
    from application.models import resource_1
    from application.tools import db
    # Create tables
    db.create_all(app=app)
    print(" * Data tables initialized : {}".format(
        resource_1.Resource_1.resource_name,
    ))
