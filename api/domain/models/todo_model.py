from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.domain.models.model_base import ModelBase


class TodoModel(ModelBase):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UserModel', back_populates='todos')
