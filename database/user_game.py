from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class UserGame(Base):
    __tablename__ = "UserGame"

    game_id = Column(ForeignKey("Game.id"), primary_key=True)
    user_id = Column(ForeignKey("User.id"), primary_key=True)

    game = relationship("Game", back_populates="game_user")
    user = relationship("User", back_populates="user_game")

    def __str__(self):
        return f"UserGame: User({self.user_id}) Game({self.game_id})"

    def __repr__(self):
        return str(self)
