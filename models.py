from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Participance(Base):
    __tablename__ = "Participance"
    id = Column(Integer, primary_key=True)
    start_num = Column(Integer)
    place_won = Column(Integer)

    # N->1
    player_id = Column(ForeignKey("Chess_players.id", ondelete="CASCADE"))
    chess_player = relationship("ChessPlayer", back_populates="participance", cascade="all,delete")

    # N->1
    championship_id = Column(ForeignKey("Championships.id", ondelete="CASCADE"))
    championship = relationship("Championship", back_populates="participance", cascade="all,delete")


class ChessPlayer(Base):
    __tablename__ = "Chess_players"
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    country = Column(String)
    rating = Column(Integer)
    title = Column(String)

    # 1->N
    participance = relationship("Participance", back_populates="chess_player")



class Championship(Base):
    __tablename__ = "Championships"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    country = Column(String)
    city = Column(String)
    date = Column(Date)
    qualification_level = Column(String)

    # 1->N
    participance = relationship("Participance", back_populates="championship")