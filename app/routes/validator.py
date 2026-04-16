from fastapi import APIRouter
from services.validation import validate
from models import Config

router =  APIRouter()


@router.post("/validate")
def validate_config(config: Config):
    return validate(config)
