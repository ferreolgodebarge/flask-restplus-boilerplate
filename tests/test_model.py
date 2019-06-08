import pytest


@pytest.mark.unit
def test_resource_1_init(database):
    from application.models.resource_1 import Resource_1
    response = Resource_1(uuid='1', name='n_test', description='d_test')
    assert response.__repr__() == ("<uuid: {}, "
                                   "name: {}, "
                                   "description: {}>").format(
        '1', 'n_test', 'd_test')
