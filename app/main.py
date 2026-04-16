from fastapi import FastAPI
from pydantic import BaseModel
import ipaddress

app = FastAPI()

class Config(BaseModel):
        hostname: str
        ip_address: ipaddress.IPv4Address
        device_type: str

@app.get("/")
def home():
        return {"message" : "Network Configuration Validatior"}

@app.post("/validate/{config_id}")
def validate(config_id : int, config: Config):
        errors = []
        if not config.hostname:
                errors.append("missing hostname")
        
        if not config.ip_address:
                errors.append("missing IP address")
        if not config.device_type:
                errors.append("missing device type")

        if config.ip_address is not ipaddress.IPv4Address:
                errors.append("invalid IP address")

        if errors:
                return {"status": "error", "errors": errors}
        return {"status": "success"}