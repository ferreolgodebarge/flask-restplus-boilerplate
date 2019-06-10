def import_blueprints(blueprints):
    from application.apis.blueprints.version import blueprint as version
    from application.apis.blueprints.v1 import blueprint as v1
    blueprint_list = [
        version,
        v1,
    ]
    return blueprint_list


def init_app(app):
    if 'VERSIONS' not in app.config:
        app.config['VERSIONS'] = "version"
    app.config['VERSIONS'] = [
        version for version in app.config['VERSIONS'].replace(
            " ", "").split(',')]
    if "version" not in app.config['VERSIONS']:
        app.config['VERSIONS'].append("version")
    for blueprint in import_blueprints(app.config['VERSIONS']):
        if blueprint.name in app.config['VERSIONS']:
            app.register_blueprint(blueprint)
            print(" * API version initialized : {}".format(blueprint.name))
