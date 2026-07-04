from app.services.generator import generate_template


def test_generate_cisco_router_config(make_config):
    config = make_config()

    result = generate_template(config)

    assert result["status"] == "success"
    assert "hostname cisco-1" in result["config"]
    assert "router ospf 1" in result["config"]


def test_generate_juniper_router_config(make_config):
    config = make_config(vendor="juniper", hostname="juniper-1")

    result = generate_template(config)

    assert result["status"] == "success"
    assert "set system host-name juniper-1" in result["config"]
    assert "set protocols ospf" in result["config"]


def test_generate_cisco_switch_config(make_config):
    config = make_config(device_type="switch", hostname="cisco-switch-1")

    result = generate_template(config)

    assert result["status"] == "success"
    assert "hostname cisco-switch-1" in result["config"]
    assert "switchport mode access" in result["config"]


def test_generate_juniper_switch_config(make_config):
    config = make_config(vendor="juniper",device_type="switch",hostname="juniper-switch-1")

    result = generate_template(config)

    assert result["status"] == "success"
    assert "set system host-name juniper-switch-1" in result["config"]
    assert "family ethernet-switching interface-mode access" in result["config"]

def test_incorrect_device_type(make_config):
    config = make_config(device_type="foo")
    result = generate_template(config)
    assert result["status"] == "error"
    assert "device type is not supported" in result["errors"]


