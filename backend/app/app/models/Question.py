from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Column, Field, SQLModel, String, ForeignKey, DateTime

class QuestionBase(SQLModel):
    repeat_count: str = Field(sa_column=Column(String))
    correct_answer_override: str = Field(sa_column=Column(String))


class QuestionCreate(QuestionBase):
    repeat_count: str
    correct_answer_override: str


class QuestionUpdate(BaseModel):
    repeat_count: Optional[str] = None
    correct_answer_override: Optional[str] = None


class Question(QuestionBase, table=True):
    __tablename__ = "Question"
    id: Optional[int] = Field(default=None, primary_key=True)
    test_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("test.id", ondelete="CASCADE")),
    )
    asset_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("asset.id", ondelete="CASCADE")),
        )
    created_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )
    updated_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True)), default_factory=datetime.utcnow
    )

class QuestionSortingFields(str, Enum):
    id = "id"
    repeat_count = "repeat_count"
    correct_answer_override = "correct_answer_override"
    test_id = "test_id"
    asset_id = "asset_id"
    created_date = "created_date"
    updated_date = "updated_date"