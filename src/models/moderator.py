from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from src.configs.database import Base


class Moderator(Base):
    __tablename__ = 'moderator'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    info = relationship('User', backref='moderator', lazy=True)
    doctor = relationship('Doctor', backref='moderators', lazy=True)
    groups = relationship('Group', backref='moderators', lazy=True)

    def __repr__(self):
        return f'<Moderator {self.info.email}>'
