import pytest
from app.services.validation import validate
from app.models import Config


@pytest.fixture
def make_config():
    def _make_config(
        hostname="cisco-1",
        ip_address="192.21.68.0",
        device_type="router",
        vendor="cisco",
        location="london-dc1",
    ):

        return Config(
            hostname=hostname,
            ip_address=ip_address,
            device_type=device_type,
            vendor=vendor,
            location=location,
        )

    return make_config


def test_correct_config(make_config):
    print("test running")
    config = make_config()
    result = validate(config)
    assert result["status"] == "success"


def test_short_hostname(make_config):
    config = make_config(hostname="foo")
    result = validate(config)
    assert result["status"] == "error"
    assert "invalid hostname - must be at least 4 characters" in result["errors"]


def test_empty_hostname(make_config):
    config = make_config(hostname="")
    result = validate(config)
    assert result["status"] == "error"
    assert "hostname is blank" in result["errors"]


def test_incorrect_vendor(make_config):
    config = make_config(vendor="nokia")
    result = validate(config)
    assert result["status"] == "error"
    assert "vendor is not supported" in result["errors"]


def test_incorrect_device_type(make_config):
    config = make_config(device_type="foo")
    result = validate(config)
    assert result["status"] == "error"
    assert "device type is not supported" in result["errors"]


def test_incorrect_location(make_config):
    config = make_config(location="bristol-dc1")
    result = validate(config)
    assert result["status"] == "error"
    assert "invalid location" in result["errors"]
