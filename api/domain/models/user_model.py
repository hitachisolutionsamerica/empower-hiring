
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from api.domain.models.model_base import ModelBase


class UserModel(ModelBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    todos = relationship('TodoModel', back_populates="user", lazy='subquery', cascade="all, delete-orphan")
