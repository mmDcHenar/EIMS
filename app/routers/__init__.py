from fastapi import APIRouter

from .product import router as product_router

api_router = APIRouter(prefix="/api")

api_router.include_router(product_router)

__all__ = ["api_router"]
