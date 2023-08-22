from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from sqlmodel import Column, Field, SQLModel, String, ForeignKey

class TestConfigBase(SQLModel):
    correct_answer_repeat_count: int
    correct_answer_repeat_increase: int


class TestConfigCreate(TestConfigBase):
    correct_answer_repeat_count: int
    correct_answer_repeat_increase: int


class TestConfigUpdate(BaseModel):
    correct_answer_repeat_count: Optional[int] = None
    correct_answer_repeat_increase: Optional[int] = None


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
   