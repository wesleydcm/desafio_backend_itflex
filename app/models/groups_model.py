from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, VARCHAR

from app.exceptions.groupsErrors import InvalidGroupError


@dataclass
class Groups(db.Model):

    code: int

    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False, unique=True)
    group_name = Column(VARCHAR(30), nullable=False, unique=True)


    @staticmethod
    def verify_group(code: int):
        if int(code) == 1:
            return {"code": code, "group_name": "Adm"}
        elif int(code) == 15:
            return {"code": code, "group_name": "Comercial"}
        elif int(code) == 30:
            return {"code": code, "group_name": "RH"}
        else:
            raise InvalidGroupError(code)
