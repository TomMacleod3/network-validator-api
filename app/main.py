from fastapi import FastAPI

from app.routes import validator
from app.routes import generator


app = FastAPI()

app.include_router(validator.router)
app.include_router(generator.router)

@app.get("/")
def home():
        return {"message" : "Network Configuration Validatior"}