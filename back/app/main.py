from fastapi import FastAPI
from app.controllers.cat_controller import router as cat_router

app = FastAPI()

app.include_router(cat_router, prefix="/api")
