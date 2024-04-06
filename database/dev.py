from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class Dev(Base):
    __tablename__ = "Dev"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    country = Column(String(25), nullable=False)
    state = Column(Integer, nullable=False)

    games = relationship("Game", back_populates="dev")

    def __str__(self):
        return f"Dev {self.id} {self.title} {self.country} {self.state}"

    def __repr__(self):
        return str(self)
