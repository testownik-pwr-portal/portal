from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.TestConfig import TestConfig, TestConfigCreate
from app.crud.crud_testConfig import crud_testconfig
from app.core.db import get_session

router = APIRouter()

@router.post("", response_model=TestConfig)
async def create_config(
    config_in: TestConfigCreate,
    db_session: Session = Depends(get_session),
) -> TestConfig:
    config = crud_testconfig.create(db=db_session, obj_in=config_in)
    return config


@router.delete("/{id}", response_model=None)
async def delete_config(
    config_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_testconfig.remove(db=db_session, id=config_id)
    return None