import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    ENV = 'TEST'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    ENV = 'DEV'
    SQLALCHEMY_DATABASE_URI = ''


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    ENV = 'STAGING'
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    """Configurations for Production."""
    ENV = 'PROD'
    SQLALCHEMY_DATABASE_URI = ''


app_config = {
    'TEST': TestingConfig,
    'DEV': DevelopmentConfig,
    'STAGING': StagingConfig,
    'PROD': ProductionConfig,
}


def init_app(
    app,
    config_file=None,
):
    print("\n##### Reload configuration #####\n")

    # Import configuration from default classes
    environment = os.environ.get('APP_ENV')
    if environment in app_config.keys():
        app.config.from_object(app_config[environment])
    else:
        print(" * Environment {} from APP_ENV variable unknown".format(
            environment))
        app.config.from_object(app_config['TEST'])

    # Import configurations from config file (.cfg)
    if config_file and os.path.exists(config_file):
        app.config.from_pyfile(config_file, silent=False)
        print(" * Configurations loaded from file: {}".format(config_file))
    else:
        print(" * No file found at this path: {}".format(config_file))
        print(" * Default Configurations loaded")
    print(" * Environment: {}".format(app.config['ENV']))
    print(" * Debug Mode: {debug}".format(
        debug="on" if app.config['DEBUG'] else "off"))
    print(" * Testing Mode: {testing}".format(
        testing="on" if app.config['TESTING'] else "off"))
    if app.config['SQLALCHEMY_DATABASE_URI'] != '':
        print(" * Database address found in configuration")
    else:
        print(" * Database address not found in configuration, \
please provide one")
        print("\n################################")
        exit(1)
    print("\n################################\n")
