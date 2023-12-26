from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from create_db import DATABASE_URI as db_url
from models import Base, Championship, ChessPlayer, Participance

DATABASE_URL = db_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def select_table(session: Session):
    results = session.query(ChessPlayer).filter(
        ChessPlayer.rating < 5000,
        ChessPlayer.title == "Grandmaster (GM)"
    ).all()
    return results

def join_tables(session: Session):
    results = session.query(ChessPlayer).join(Participance, ChessPlayer.id == Participance.player_id).all()
    return results

def update_table(session: Session):
    session.query(ChessPlayer).filter(ChessPlayer.rating < 5000).update({ChessPlayer.title: "Grandmaster (GM)"})
    session.commit()

def group_by_field(session: Session):
    results = session.query(func.count(Championship.country), Championship.country).group_by(Championship.country).all()
    return results

def sort_results(session: Session, sort_field: str='date'):
    results = session.query(Championship).order_by(getattr(Championship, sort_field)).all()
    return results


session.close()




