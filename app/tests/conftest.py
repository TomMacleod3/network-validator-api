import pytest
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

    return _make_config
