from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from .base import Base, SessionLocal, engine


class GetDB:  # Context Manager
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, SQLAlchemyError):
            self.db.rollback()  # rollback on exception

        self.db.close()


def get_db():  # Dependency
    with GetDB() as db:
        yield db


__all__ = [
    "GetDB",
    "get_db",
    "Base",
    "Session",
]
