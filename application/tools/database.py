from flask_sqlalchemy import SQLAlchemy


class Database():
    def __init__(self):
        self.db = SQLAlchemy()
        self.initialized = False

    def init_app(self, app):
        self.db.init_app(app)
        self.initialized = True
        print(" * Database initialized")
