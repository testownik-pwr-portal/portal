from app.crud.base import CRUDBase
from app.models.TestPrivilige import TestPrivi, TestPriviCreate, TestPriviUpdate


class CRUDTestPrivi(CRUDBase[TestPrivi, TestPriviCreate,TestPriviUpdate]):
    pass

crud_testprivi = CRUDTestPrivi(TestPrivi)