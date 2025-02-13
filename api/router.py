from fastapi import APIRouter
from api.routes import books
from core.config import settings

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
