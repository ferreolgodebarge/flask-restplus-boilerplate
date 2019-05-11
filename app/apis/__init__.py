from app.apis.v1 import blueprint as v1


def init_app(app):
    app.register_blueprint(v1)
