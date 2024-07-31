from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Vaccination(BaseModel):
    type: str
    date: datetime

class Cat(BaseModel):
    name: str
    age: int
    breed: str
    image: str
    vaccinations: List[Vaccination]
    id : Optional[str] = None