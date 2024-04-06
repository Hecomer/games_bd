from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class Game(Base):
    __tablename__ = "Game"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    pg = Column(Integer, nullable=False)
    gpu = Column(String(100), nullable=False)
    cpu = Column(String(100), nullable=False)
    ram = Column(Integer, nullable=False)
    disc_space = Column(Integer, nullable=False)
    os = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.id"))
    user_rating = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    dev_id = Column(Integer, ForeignKey("Dev.id"))

    category = relationship("Category", back_populates="games")
    dev = relationship("Dev", back_populates="games")
    game_user = relationship("UserGame", back_populates="game")
    review = relationship("Review", back_populates="game")

    def __str__(self):
        return f"Game {self.id} {self.title} {self.price} {self.pg} {self.gpu} {self.cpu} {self.ram} {self.disc_space} \
            {self.os} {self.category_id} {self.user_rating} {self.year} {self.dev_id}"

    def __repr__(self):
        return str(self)
