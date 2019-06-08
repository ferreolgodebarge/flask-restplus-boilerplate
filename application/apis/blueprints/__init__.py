def import_blueprints(blueprints):
    from importlib import import_module
    blueprint_list = [getattr(import_module(
        f"{__name__}.{blueprint}"), "blueprint") for blueprint in blueprints]
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
        app.register_blueprint(blueprint)
        print(" * API version initialized : {}".format(blueprint.name))
