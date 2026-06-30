from fastapi import APIRouter
from app.services.generator import generate_template
from app.models import Config


router =  APIRouter()


@router.post("/generate-config")
def generate_config(config: Config):
    if config.device_type == "router":
        return generate_template(config,"router_config.j2")
    elif config.device_type == "switch":
        return generate_template(config,"switch_config.j2")