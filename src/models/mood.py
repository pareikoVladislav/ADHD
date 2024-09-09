from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.configs.database import Base

class Mood(Base):
    __tablename__ = 'mood'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    photo = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    patient_logs = relationship('PatientMoodLog', backref='mood')

    def __repr__(self):
        return f'{self.description[:7]}...'
