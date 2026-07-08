from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import validator
from app.routes import generator


app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(validator.router)
app.include_router(generator.router)

@app.get("/")
def home():
        return {"message" : "Network Configuration Validatior"}