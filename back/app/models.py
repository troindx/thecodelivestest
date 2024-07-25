from pydantic import BaseModel
from typing import List
from datetime import datetime

class Vaccination(BaseModel):
    type: str
    date: datetime

class Cat(BaseModel):
    name: str
    age: int
    breed: str
    vaccinations: List[Vaccination]