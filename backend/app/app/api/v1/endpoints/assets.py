from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.asset import asset, assetCreate
from app.crud.crud_asset import crud_asset
from app.core.db import get_session

router = APIRouter()

@router.post("", response_model=asset)
async def create_asset(
    asset_in: assetCreate,
    db_session: Session = Depends(get_session),
) -> asset:
    asset = crud_asset.create(db=db_session, obj_in=asset_in)
    return asset


@router.delete("/{id}", response_model=None)
async def delete_asset(
    asset_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_asset.remove(db=db_session, id=asset_id)
    return None