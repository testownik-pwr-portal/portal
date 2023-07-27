from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.Test import Test, TestCreate
from app.crud.crud_test import crud_test
from app.core.db import get_session

router = APIRouter()

@router.post("", response_model=Test)
async def create_test(
    test_in: TestCreate,
    db_session: Session = Depends(get_session),
) -> Test:
    test = crud_test.create(db=db_session, obj_in=test_in)
    return test


@router.delete("/{id}", response_model=None)
async def delete_test(
    test_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_test.remove(db=db_session, id=test_id)
    return None