from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/validate")
def validate_config(config: dict):
    errors = []

    if "hostname" not in config:
        errors.append("Missing hostname")

    if "ip_address" not in config:
        errors.append("Missing ip_address")

    if "device_type" not in config:
        errors.append("Missing device_type")

    if config.get("device_type") not in ["router", "switch", "firewall"]:
        errors.append("Invalid device_type")

    if errors:
        return {"status": "error", "errors": errors}

    return {"status": "success"}