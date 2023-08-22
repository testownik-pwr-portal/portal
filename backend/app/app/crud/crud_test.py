from app.crud.base import CRUDBase
from app.models.Test import Test, TestCreate, TestUpdate


class CRUDTest(CRUDBase[Test, TestCreate,TestUpdate]):
    pass

crud_test = CRUDTest(Test)