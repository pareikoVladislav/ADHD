from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from src.configs.database import Base

class Role(Base):
    __tablename__ = 'role'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    type = Column(String(75), nullable=False)

    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role {self.type}'
