from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Column, Field, SQLModel, String, ForeignKey

class TestConfigBase(SQLModel):
    correct_answer_repeat_count: str = Field(sa_column=Column(String))
    correct_answer_repeat_increase: str = Field(sa_column=Column(String))


class TestConfigCreate(TestConfigBase):
    correct_answer_repeat_count: str
    correct_answer_repeat_increase: str


class TestConfigUpdate(BaseModel):
    correct_answer_repeat_count: Optional[str] = None
    correct_answer_repeat_increase: Optional[str] = None


class TestConfig(TestConfigBase, table=True):
    __tablename__ = "TestConfig"
    id: Optional[int] = Field(default=None, primary_key=True)
    test_id: Optional[int] = Field(
        default=None,
        sa_column=Column(ForeignKey("test.id", ondelete="CASCADE")),
    )

class TestConfigSortingFields(str, Enum):
    id = "id"
    correct_answer_repeat_count = "correct_answer_repeat_count"
    correct_answer_repeat_increase = "correct_answer_repeat_increase"
    test_id = "test_id"
   