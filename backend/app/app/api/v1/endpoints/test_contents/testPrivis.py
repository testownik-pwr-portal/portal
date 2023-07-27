from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.TestPrivilige import TestPrivi, TestPriviCreate
from app.crud.crud_testPrivi import crud_testprivi
from app.core.db import get_session

router = APIRouter()

@router.post("", response_model=TestPrivi)
async def create_privi(
    privi_in: TestPriviCreate,
    db_session: Session = Depends(get_session),
) -> TestPrivi:
    privi = crud_testprivi.create(db=db_session, obj_in=privi_in)
    return privi


@router.delete("/{id}", response_model=None)
async def delete_privi(
    privi_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_testprivi.remove(db=db_session, id=privi_id)
    return None