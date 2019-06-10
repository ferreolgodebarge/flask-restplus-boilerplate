import os


def create_app(
    config_file=os.path.join(os.path.split(
        os.path.split(os.path.realpath(__name__))[0])[0],
        'settings.cfg'),
):
    """[Create Flask application]

    Keyword Arguments:
        config_file {[String]} -- [Load a .cfg file if exists to configure app]
            (default:
                {os.path.join(os.path.split(os.path.split(
                    os.path.realpath(__name__))[0])[0],'settings.cfg')}
            )

    Returns:
        [type] -- [description]
    """
    # Init Flask app
    from flask import Flask
    app = Flask(__name__)

    # Load configuration
    from application import config
    config.init_app(app, config_file)

    # Init database
    from application.tools import database
    database.init_app(app)

    # Init Database tables
    from application import models
    models.init_app(app)

    # Init apis
    from application.apis import blueprints
    blueprints.init_app(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(use_reloader=False)
