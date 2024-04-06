from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class Review(Base):
    __tablename__ = "Review"

    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    game_id = Column(ForeignKey("Game.id"), primary_key=True)
    user_id = Column(ForeignKey("User.id"), primary_key=True)

    game = relationship("Game", back_populates="review")
    user = relationship("User", back_populates="review")

    def __str__(self):
        return f"Game {self.id} {self.title}"

    def __repr__(self):
        return str(self)
