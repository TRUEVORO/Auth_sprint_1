from sqlalchemy import Column, ForeignKey, Table

from extensions import db

user_role = Table(
    'user_role',
    db.metadata,
    Column('user_id', ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    Column('role_id', ForeignKey('role.id', ondelete='CASCADE'), primary_key=True),
)
