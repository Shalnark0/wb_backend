from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import products

app = FastAPI()

app.include_router(products.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)