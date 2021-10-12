from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta

from app.configs.database import db
from app.models.certificates_groups_table import certificates_groups
from app.models.groups_model import Groups
from sqlalchemy import DATE, VARCHAR, Column, Integer, Text
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import DateTime


@dataclass
class Certificates(db.Model):

    id: int
    username: str
    name: str
    description: str
    expiration: int
    expirated_at: DateTime
    created_at: DateTime
    updated_at: DateTime
    groups: list = field(default_factory=list)


    __tablename__ = 'certificates'


    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(30), nullable=False, unique=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(Text)
    expiration = Column(Integer, nullable=False)
    expirated_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    groups = relationship('Groups', secondary=certificates_groups, backref=backref("certificates", uselist=True))


    @staticmethod
    def insert_dates_new_certificates(data):
        
        expiration: int = data['expiration']

        data["expirated_at"] = (datetime.utcnow() + timedelta(days=expiration))
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)

        return data
