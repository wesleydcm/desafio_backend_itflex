import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

from app.configs.database import db
from app.models.certificates_groups_table import certificates_groups
from app.models.groups_model import Groups
from sqlalchemy import VARCHAR, Column, Integer, Text
from sqlalchemy.orm import backref, relationship, validates
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

    @validates('username')
    def validate_username(self, key, username):

        pattern_username = re.compile(r"^([a-z]|[0-9]){3,30}$")
        result = re.fullmatch(pattern_username, username)

        if not result:
          raise ValueError('field `username` allows characters `a-z` and `0-9` and maximum characters must be 30')

        return username


    @validates('name')
    def validate_name(self, key, name):

        if len(name) > 255 or len(name) < 1:
          raise ValueError('field name is mandatory and maximum characters must be 255')

        return name


    @validates('expiration')
    def validate_name(self, key, expiration):

        if expiration < 10 or expiration > 3650:
          raise ValueError('The "expiration" field represents the number of days the certificate is valid, it must be between 10 and 3650.')

        return expiration
