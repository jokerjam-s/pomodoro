from sqlalchemy import select
from database.database import Session
from database import Tasks


class TaskRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def get_all_tasks(self):
        pass

    def get_task_by_id(self, task_id):
        query = select(Tasks).where(Tasks.id == self.session.id)
        with self.session as session:
            tasks = session.execute(query).scalar()
        return tasks


def get_task_repository() -> TaskRepository:
    db_session = Session()
    return TaskRepository(db_session)
