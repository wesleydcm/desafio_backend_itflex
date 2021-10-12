from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer

certificates_groups = db.Table('certificates_groups',
    Column('certificate_group_id', Integer, primary_key=True),
    Column('certificate_id', Integer, ForeignKey('certificates.id')),
    Column('group_id', Integer, ForeignKey('groups.group_id'))
)
