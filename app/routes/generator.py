from fastapi import APIRouter
from app.services.generator import generate_template
from app.models import Config


router =  APIRouter()


@router.post("/generate")
def generate_config(config: Config):
        return generate_template(config)