from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from src.configs.database import Base

class Patient(Base):
    __tablename__ = 'patient'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_age_id = Column(Integer, ForeignKey('group_age.id'), nullable=False)
    restore_notification = Column(Boolean, nullable=False, default=False)

    mood_logs = relationship('PatientMoodLog', backref='patient')
    info = relationship('User', backref='patient')

    def __repr__(self):
        return f'<Patient {self.info.full_name}>'