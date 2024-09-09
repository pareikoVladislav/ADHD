from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.configs.database import Base



class Doctor(Base):
    __tablename__ = 'doctor'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    specialisation = Column(String(75), nullable=False)
    phone = Column(String(75), nullable=False)


    groups = relationship('Group', backref='doctor', lazy=True)
    moderators = relationship('Moderator', backref='doctor', lazy=True)

    def __repr__(self):
        return f'<Doctor {self.id}>'
