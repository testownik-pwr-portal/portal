from typing import Optional
from sqlmodel import Session, select
from app.models.asset import asset, assetCreate, assetUpdate
from app.crud.base import CRUDBase

class CRUDAsset(CRUDBase[asset, assetCreate, assetUpdate]):
    def get_by_contents(self, db: Session, *, contents: str) -> Optional[asset]:
        return db.exec(select(asset).where(asset.contents == contents)).first()

crud_asset = CRUDAsset(asset)