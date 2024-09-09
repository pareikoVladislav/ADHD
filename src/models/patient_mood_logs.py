from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.configs.database import Base

class PatientMoodLog(Base):
    __tablename__ = 'patient_mood_log'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    patient_id = Column(Integer, ForeignKey('patient.id'))
    mood_id = Column(Integer, ForeignKey('mood.id'))
    scale = Column(String(255), nullable=False)
    segments_in_a_day = Column(String, nullable=True)

    patient = relationship('Patient', backref='mood_logs')
    mood = relationship('Mood', backref='patient_logs')
