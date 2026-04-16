from fastapi import FastAPI

from routes import validator


app = FastAPI()

app.include_router(validator.router)

@app.get("/")
def home():
        return {"message" : "Network Configuration Validatior"}