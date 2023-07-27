from app.crud.base import CRUDBase
from app.models.TestConfig import TestConfig, TestConfigCreate, TestConfigUpdate

class CRUDTestConfig(CRUDBase[TestConfig, TestConfigCreate,TestConfigUpdate]):
    pass

crud_testconfig = CRUDTestConfig(TestConfig)