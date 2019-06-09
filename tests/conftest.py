import pytest
import os
import shutil

from application.app import create_app


@pytest.fixture
def app():
    yield create_app()


@pytest.fixture
def app_no_env():
    if 'APP_ENV' in os.environ:
        os.environ.pop('APP_ENV')
    yield create_app()


@pytest.fixture
def app_no_env_with_file():
    if 'APP_ENV' in os.environ:
        os.environ.pop('APP_ENV')
    test_settings = os.path.join(
        os.getcwd(),
        'tests',
        'test_files',
        'test_settings.cfg',
    )
    settings = os.path.join(os.getcwd(), 'settings.cfg')
    shutil.copyfile(test_settings, settings)
    yield create_app()
    os.remove(settings)


@pytest.fixture
def create_app_test():
    return create_app


@pytest.fixture
def app_dev_with_config_file():
    os.environ['APP_ENV'] = 'DEV'
    test_settings = os.path.join(
        os.getcwd(),
        'tests',
        'test_files',
        'test_settings.cfg',
    )
    settings = os.path.join(os.getcwd(), 'settings.cfg')
    shutil.copyfile(test_settings, settings)
    yield create_app()
    os.remove(settings)


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    yield client


@pytest.fixture
def client_v1():
    test_settings = os.path.join(
        os.getcwd(),
        'tests',
        'test_files',
        'test_settings.cfg',
    )
    settings = os.path.join(os.getcwd(), 'settings.cfg')
    shutil.copyfile(test_settings, settings)
    app = create_app()
    os.remove(settings)
    client = app.test_client()
    yield client


@pytest.fixture
def client_v1_backend_issue(monkeypatch):
    test_settings = os.path.join(
        os.getcwd(),
        'tests',
        'test_files',
        'test_settings.cfg',
    )
    settings = os.path.join(os.getcwd(), 'settings.cfg')
    shutil.copyfile(test_settings, settings)
    monkeypatch.setattr("application.models.init_app", lambda x: '')
    app = create_app()
    os.remove(settings)
    client = app.test_client()
    yield client


@pytest.fixture
def database():
    from flask_sqlalchemy import SQLAlchemy
    return SQLAlchemy()
