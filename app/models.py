from pydantic import BaseModel
import ipaddress

class Config(BaseModel):
        hostname: str
        ip_address: ipaddress.IPv4Address
        device_type: str