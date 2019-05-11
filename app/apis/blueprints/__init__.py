def import_blueprints(blueprints):
    from importlib import import_module
    blueprint_list = [getattr(import_module(
        f"{__name__}.{blueprint}"), "blueprint") for blueprint in blueprints]
    return blueprint_list


def init_app(app):
    app.config['VERSIONS'] = [
        version for version in app.config['VERSIONS'].replace(
            " ", "").split(',')]
    for blueprint in import_blueprints(app.config['VERSIONS']):
        app.register_blueprint(blueprint)
