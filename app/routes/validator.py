from fastapi import APIRouter
from app.services.validation import validate
from app.models import Config


router =  APIRouter()


@router.post("/validate")
def validate_config(config: Config):
    return validate(config)
