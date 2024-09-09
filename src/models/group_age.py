from sqlalchemy import Column, Integer


from src.configs.database import Base


class GroupAge(Base):
    __tablename__ = 'group_age'
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True,
        unique=True
    )
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<GroupAge({self.age})>'
