from flask_sqlalchemy import SQLAlchemy


class Database():
    """[Database class to init SQLAlchemy db]
    """
    def __init__(self):
        """[Initializer]
        """
        self.db = SQLAlchemy()
        self.initialized = False

    def init_app(self, app):
        """[Load database in app context]

        Arguments:
            app {[Flask]} -- [Flask application]
        """
        self.db.init_app(app)
        self.initialized = True
        print(" * Database initialized")
