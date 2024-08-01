from fastapi import APIRouter, HTTPException
from app.services.cat_service import CatService
from app.models import Cat
from typing import List

from app.services.config_service import ConfigService


router = APIRouter()
config_service = ConfigService()
cat_service = CatService(config_service)

@router.post("/cats/", response_model=str)
def create_cat(cat: Cat):
    cat_id = cat_service.create_cat(cat)
    return cat_id

@router.get("/cats/{cat_id}", response_model=Cat)
def read_cat(cat_id: str):
    cat = cat_service.get_cat(cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat

@router.put("/cats/{cat_id}", response_model=bool)
def update_cat(cat_id: str, cat: Cat):
    success = cat_service.update_cat(cat_id, cat)
    if not success:
        raise HTTPException(status_code=404, detail="Cat not found")
    return success

@router.delete("/cats/{cat_id}", response_model=bool)
def delete_cat(cat_id: str):
    success = cat_service.delete_cat(cat_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cat not found")
    return success

@router.get("/cats/", response_model=List[Cat])
def list_cats():
    return cat_service.list_cats()
