def create_app():
    # Create flask application
    from flask import Flask
    app = Flask(__name__)

    # Init database
    from app.models import db
    db.init_app(app)

    # Init apis

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
