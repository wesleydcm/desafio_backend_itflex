from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.sql.sqltypes import Text


@dataclass
class Groups(db.Model):

    code: int

    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    code = Column(Integer(100), nullable=False, unique=True)
    group_name = Column(VARCHAR(30), nullable=False, unique=True)
