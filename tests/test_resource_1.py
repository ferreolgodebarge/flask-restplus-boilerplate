import pytest


@pytest.mark.unit
def test_namespace_resource_1_list_empty(client_v1):
    expected_response = []
    expected_status_code = 200
    res = client_v1.get('/api/v1/resource-1')
    assert res.status_code == expected_status_code
    assert res.json == expected_response


@pytest.mark.unit
def test_namespce_resource_1_create(client_v1, monkeypatch):
    expected_post_response = {
        "name": "n_test",
        "description": "d_test",
        "id": "id_test",
    }
    expected_post_status_code = 201
    payload = {"name": "n_test", "description": "d_test"}
    monkeypatch.setattr("uuid.uuid4", lambda: 'id_test')
    res = client_v1.post('/api/v1/resource-1', json=payload)
    assert res.status_code == expected_post_status_code
    assert res.json == expected_post_response

    expected_list_response = [{
        "name": "n_test",
        "description": "d_test",
        "id": "id_test",
    }]
    expected_list_status_code = 200
    res = client_v1.get('/api/v1/resource-1')
    assert res.status_code == expected_list_status_code
    assert res.json == expected_list_response


@pytest.mark.unit
def test_namespce_resource_1_get(client_v1):
    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1.post('/api/v1/resource-1', json=payload)

    expected_get_response = res.json
    expected_get_status_code = 200
    res = client_v1.get('/api/v1/resource-1/{}'.format(res.json['id']))
    assert res.status_code == expected_get_status_code
    assert res.json == expected_get_response


@pytest.mark.unit
def test_namespace_resource_1_create_conflict(client_v1):
    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1.post('/api/v1/resource-1', json=payload)
    assert res.status_code == 201

    res = client_v1.post('/api/v1/resource-1', json=payload)
    assert res.status_code == 409


@pytest.mark.unit
def test_namespace_resource_1_put(client_v1):
    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1.post('/api/v1/resource-1', json=payload)
    assert res.status_code == 201

    payload = {"name": "n_test_up", "description": "d_test_up"}
    res = client_v1.put(
        '/api/v1/resource-1/{}'.format(res.json['id']), json=payload)
    expected_response = payload
    expected_response['id'] = res.json['id']
    expected_status_code = 200

    assert res.status_code == expected_status_code
    assert res.json == expected_response


@pytest.mark.unit
def test_namespace_resource_1_delete(client_v1):
    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1.post('/api/v1/resource-1', json=payload)
    assert res.status_code == 201

    res = client_v1.delete('/api/v1/resource-1/{}'.format(res.json['id']))
    expected_status_code = 204
    assert res.data == b''
    assert res.status_code == expected_status_code


@pytest.mark.unit
def test_namespace_resource_1_get_put_delete_not_found(client_v1):
    expected_response = {
        "status": "FAILED",
        "message": "Resource 1 not found",
    }
    expected_status_code = 404
    res = client_v1.get('/api/v1/resource-1/1')
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1.put('/api/v1/resource-1/1', json=payload)
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    res = client_v1.delete('/api/v1/resource-1/1')
    assert res.status_code == expected_status_code
    assert res.json == expected_response


@pytest.mark.unit
def test_resource_1_backend_issue(client_v1_backend_issue):
    expected_response = {
        "status": "FAILED",
        "message": "Unable to contact backend",
    }
    expected_status_code = 503

    res = client_v1_backend_issue.get('/api/v1/resource-1')
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    payload = {"name": "n_test", "description": "d_test"}
    res = client_v1_backend_issue.post('/api/v1/resource-1', json=payload)
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    res = client_v1_backend_issue.get("/api/v1/resource-1/1")
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    res = client_v1_backend_issue.put("/api/v1/resource-1/1", json=payload)
    assert res.status_code == expected_status_code
    assert res.json == expected_response

    res = client_v1_backend_issue.delete("/api/v1/resource-1/1")
    assert res.status_code == expected_status_code
    assert res.json == expected_response
