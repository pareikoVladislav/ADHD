from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp

from src.configs.database import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    full_name = Column(String(175), nullable=True)
    photo = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    password = Column(String(255), nullable=False)
    image_password = Column(String(255), nullable=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=True)
    is_doctor = Column(Boolean, nullable=False, default=False)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=True)
    date_join = Column(DateTime, nullable=False, server_default=current_timestamp())

    doctor_info = relationship('Doctor', backref='user')

    def __repr__(self):
        return f'<User({self.email})>'
