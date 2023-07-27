from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, SQLModel, String

class TestBase(SQLModel):
    name: str = Field(sa_column=Column(String))
    description: str = Field(sa_column=Column(String))


class TestCreate(TestBase):
    name: str
    description: str


class TestUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Test(TestBase, table=True):
    __tablename__ = "test"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )


class TestPriviSortingFields(str, Enum):
    id = "id"
    name = "name"
    description = "description"
    created_date = "created_date"
    updated_date = "updated_date"
   