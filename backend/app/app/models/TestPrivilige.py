from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Column, DateTime, Field, ForeignKey, SQLModel, String


class TestPriviBase(SQLModel):
    role: 'Roles' = Field(sa_column=Column(String))


class TestPriviCreate(TestPriviBase):
    role: 'Roles'


class TestPriviUpdate(BaseModel):
    role: Optional['Roles'] = None    


class TestPrivi(TestPriviBase, table=True):
    __tablename__ = "TestPrivilige"
    user_id: Optional[int] = Field(default=None, primary_key=True)
    test_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("test.id", ondelete="CASCADE")),
    )
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )

class Roles(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"

class TestPriviSortingFields(str, Enum):
    id = "id"
    role = "role"
    created_date = "created_date"
    updated_date = "updated_date"