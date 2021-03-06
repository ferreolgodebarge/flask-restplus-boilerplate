import os


def create_app(
    config_file=os.path.join(os.getcwd(), 'settings.cfg'),
):
    # Init Flask app
    from flask import Flask
    app = Flask(__name__)

    # Load configuration
    from . import config
    config.init_app(app, config_file)

    # Init database
    from .tools import database
    database.init_app(app)

    # Init Database tables
    from . import models
    models.init_app(app)

    # Init apis
    from .apis import blueprints
    blueprints.init_app(app)

    return app


app = create_app()
