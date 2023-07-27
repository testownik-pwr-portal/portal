from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.Question import Question, QuestionCreate
from app.crud.crud_question import crud_question
from app.core.db import get_session

router = APIRouter()

@router.post("", response_model=Question)
async def create_question(
    question_in: QuestionCreate,
    db_session: Session = Depends(get_session),
) -> Question:
    question = crud_question.create(db=db_session, obj_in=question_in)
    return question


@router.delete("/{id}", response_model=None)
async def delete_question(
    question_id: int,
    db_session: Session = Depends(get_session),
) -> None:
    crud_question.remove(db=db_session, id=question_id)
    return None