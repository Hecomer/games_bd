from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100), nullable=False)

    user_game = relationship("UserGame", back_populates="user")
    review = relationship("Review", back_populates="user")

    def __str__(self):
        return f"User {self.id} {self.nickname}"

    def __repr__(self):
        return str(self)
