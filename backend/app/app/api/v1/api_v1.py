from fastapi import APIRouter

from app.api.v1.endpoints.login import router as login_router
from app.api.v1.endpoints.users import router as users_router
from app.api.v1.endpoints.assets import router as assets_router
from api.v1.endpoints.tests import router as tests_router

api_v1_router = APIRouter()

api_v1_router.include_router(users_router, prefix="/users", tags=["users"])
api_v1_router.include_router(login_router, prefix="/login", tags=["login"])
api_v1_router.include_router(assets_router, prefix="/assets", tags=["assets"])
api_v1_router.include_router(tests_router, prefix="/tests", tags=["tests"])

