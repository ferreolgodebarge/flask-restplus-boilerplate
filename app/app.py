def create_app():
    # Create flask application
    from flask import Flask
    app = Flask(__name__)

    # Import configurations
    app.config.from_object('app.config.conf')

    # Init database
    import app.models as db
    db.init_app(app)

    # Init apis
    import app.apis.blueprints as apis
    apis.init_app(app)

    return app
