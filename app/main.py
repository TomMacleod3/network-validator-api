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
        if config.hostname.strip() == "":
                errors.append("hostname is blank")
        elif len(config.hostname) < 4:
                errors.append("invalid hostname - must be at least 4 characters")
        
        if config.device_type not in {"router", "switch", "firewall"}:
                errors.append("device type is not supported")

        if errors:
                return {"status": "error", "errors": errors}
        return {"status": "success"}