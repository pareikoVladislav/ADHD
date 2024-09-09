from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from sqlalchemy.sql.functions import current_timestamp

from src.configs.database import Base


class Group(Base):
    __tablename__ = 'group'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    name = Column(String(100), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())

    doctor = relationship('Doctor', backref='groups')

    def __repr__(self):
        return f'<Group({self.name})>'
