from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_generate_route_valid_config_returns_200(make_config):
    payload = make_config()
    payload = payload.model_dump(mode="json")
    response = client.post("/generate", json = payload)
    assert response.status_code == 200

def test_validate_route_valid_payload_returns_success(make_config):
    payload = make_config()
    payload = payload.model_dump(mode="json")
    response = client.post("/generate", json = payload)
    print(response.json())
    assert response.json()["status"] == 'success'

# invalid IP address cannot be tested from the class in netconf.py as it will not pass Pydantic rules
def test_invalid_ip_returns_422():
    response = client.post(
        "/generate",
        json={
            "hostname": "cisco-1",
            "ip_address": "bad-ip",
            "device_type": "router",
            "vendor": "cisco",
            "location": "london-dc1",
        },
    )
    assert response.status_code == 422