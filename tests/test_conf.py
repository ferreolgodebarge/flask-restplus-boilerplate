import pytest
import os


@pytest.mark.unit
def test_config_from_environment_no_ENV(app_no_env):
    assert app_no_env.config['ENV'] == 'TEST'
    assert app_no_env.config['DEBUG']
    assert app_no_env.config['TESTING']
    assert app_no_env.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'


@pytest.mark.unit
def test_config_DEV_from_environment(app_dev_with_config_file):
    assert app_dev_with_config_file.config['ENV'] == 'DEV'
    assert app_dev_with_config_file.config['DEBUG']


@pytest.mark.unit
@pytest.mark.parametrize("env", ['DEV', 'STAGING', 'PROD'])
def test_config_ENV_without_file_error(env, create_app_test):
    os.environ['APP_ENV'] = env
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_app_test()
    assert pytest_wrapped_e.value.code == 1


@pytest.mark.unit
@pytest.mark.parametrize("env", ['TEST'])
def test_config_TEST_without_file_pass(env, create_app_test):
    os.environ['APP_ENV'] = env
    app = create_app_test()
    assert app.config['ENV'] == 'TEST'


@pytest.mark.unit
def test_blueprint_init_app_without_file(app_no_env):
    expected = ["version", "restplus_doc"]
    assert len(app_no_env.blueprints) == len(expected)
    for e in expected:
        assert e in app_no_env.blueprints


@pytest.mark.unit
def test_blueprint_init_app_with_file_add_version(app_no_env_with_file):
    expected = ["v1", "version", "restplus_doc"]
    assert len(app_no_env_with_file.blueprints) == len(expected)
    for e in expected:
        assert e in app_no_env_with_file.blueprints
