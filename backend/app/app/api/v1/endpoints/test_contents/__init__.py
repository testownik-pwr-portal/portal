from fastapi import APIRouter


from app.api.v1.endpoints.test_contents.questions import router as questions_router
from app.api.v1.endpoints.test_contents.testConfigs import router as configs_router
from app.api.v1.endpoints.test_contents.testPrivis import router as privis_router
from app.api.v1.endpoints.test_contents.tests import router as tests_router


router = APIRouter()

router.include_router(questions_router, prefix="/testconfigs", tags=["questions"])
router.include_router(configs_router, prefix="/testconfigs", tags=["configs"])
router.include_router(privis_router, prefix="/testconfigs", tags=["privis"])
router.include_router(tests_router, prefix="/testconfigs", tags=["tests"])