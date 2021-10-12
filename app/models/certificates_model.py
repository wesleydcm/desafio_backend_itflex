from dataclasses import dataclass, field


from app.configs.database import db
from app.models.certificates_groups_table import certificates_groups
from app.models.groups_model import Groups
from sqlalchemy import Column, Integer, VARCHAR, Text, DATE
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import ForeignKey


@dataclass
class Certificates(db.Model):

    id: int
    name: str
    description: str
    duration: int
    groups: list = field(default_factory=list)


    __tablename__ = 'cestificates'


    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(30), nullable=False, unique=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(Text)
    expiration = Column(Integer, nullable=False)
    expirated_at = Column(DATE, nullable=False)
    created_at = Column(DATE, nullable=False)
    updated_at = Column(DATE, nullable=False)

    groups = relationship('Groups', secondary=certificates_groups, backref=backref("cestificates", uselist=True))
