import pytest


@pytest.mark.unit
def test_namespace_version_get(client):
    expected_response = "not yet implemented"
    expected_status_code = 200
    res = client.get('/api/version')
    assert res.status_code == expected_status_code
    assert res.json == expected_response
