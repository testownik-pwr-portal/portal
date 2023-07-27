from app.crud.base import CRUDBase
from app.models.Question import Question, QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):
    pass

crud_question = CRUDQuestion(Question)