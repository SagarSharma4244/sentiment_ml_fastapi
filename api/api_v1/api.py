from fastapi import APIRouter
from .endpoints import cities
from .endpoints import ml

router = APIRouter()
router.include_router(cities.router, prefix="/cities",tags=["Cities"])
router.include_router(ml.router, prefix="/ml",tags=["ML"])