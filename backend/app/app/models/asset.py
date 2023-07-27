from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, SQLModel, String


class assetBase(SQLModel):
    contents: str = Field(sa_column=Column(String))

class assetCreate(assetBase):
    contents: str

class assetUpdate(BaseModel):
    contents: Optional[str] = None

class asset(assetBase, table=True):
    __tablename__ = "asset"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )

class assetSortingFields(str, Enum):
    id = "id"
    created_date = "created_date"
    updated_date = "updated_date"
    contents = "contents"