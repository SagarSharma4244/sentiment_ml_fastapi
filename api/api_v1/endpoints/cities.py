from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
class City(BaseModel):
    name:str
    timezone:str

# cities
@router.get('/')
async def get_cities():
    return db


@router.get('/{city_id}')
def get_single_cities():
    return db[city_id]


@router.post('/')
def create_city(city: City):
    db.append(city.dict())
    return db

@router.delete('/{city_id}')
def delete_create(city_id: int):
    db.pop(city_id)
    return db