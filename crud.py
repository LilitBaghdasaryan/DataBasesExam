from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Championship, ChessPlayer, Participance
from schemes import ChessPlayerCreate, ChessPlayerResponse, ChampionshipCreate, ChampionshipResponse, ParticipanceCreate, ParticipanceResponse
from create_db import DATABASE_URI as db_url
import uvicorn
from typing import List

app = FastAPI()

DATABASE_URL = db_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

                                #*** Chess player CRUD ***#

@app.post("/chess_players/", response_model=ChessPlayerResponse)
def create_player(player: ChessPlayerCreate, db: Session = Depends(get_db)):
    db_player = ChessPlayer(**player.model_dump())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

@app.get("/chess_players/{player_id}", response_model=ChessPlayerResponse)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(ChessPlayer).filter(ChessPlayer.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@app.get("/chess_players/", response_model=List[ChessPlayerResponse])
def get_all_players(db: Session = Depends(get_db)):
    chess_players = db.query(ChessPlayer).all()
    return chess_players

@app.put("/chess_players/{player_id}", response_model=ChessPlayerResponse)
def update_player(player_id: int, updated_player: ChessPlayerCreate, db: Session = Depends(get_db)):
    db_player = db.query(ChessPlayer).filter(ChessPlayer.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    for field, value in updated_player.model_dump().items():
        setattr(db_player, field, value)

    db.commit()
    db.refresh(db_player)
    return db_player

@app.delete("/chess_players/{player_id}", response_model=ChessPlayerResponse)
def delete_player(player_id: int, db: Session = Depends(get_db)):
    db_player = db.query(ChessPlayer).filter(ChessPlayer.id == player_id).first()
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    db.delete(db_player)
    db.commit()
    return db_player


                                #*** Championship CRUD ***#

@app.post("/championships/", response_model=ChampionshipResponse)
def create_championship(championship: ChampionshipCreate, db: Session = Depends(get_db)):
    db_championship = Championship(**championship.model_dump())
    db.add(db_championship)
    db.commit()
    db.refresh(db_championship)
    return db_championship

@app.get("/championships/{championship_id}", response_model=ChampionshipResponse)
def read_championship(championship_id: int, db: Session = Depends(get_db)):
    db_championship = db.query(Championship).filter(Championship.id == championship_id).first()
    if db_championship is None:
        raise HTTPException(status_code=404, detail="Championship not found")
    return db_championship

@app.get("/championships/", response_model=List[ChampionshipResponse])
def get_all_championships(db: Session = Depends(get_db)):
    championships = db.query(Championship).all()
    return championships

@app.put("/championships/{championship_id}", response_model=ChampionshipResponse)
def update_championship(championship_id: int, updated_championship: ChampionshipCreate, db: Session = Depends(get_db)):
    db_championship = db.query(Championship).filter(Championship.id == championship_id).first()
    if db_championship is None:
        raise HTTPException(status_code=404, detail="Championship not found")

    for field, value in updated_championship.model_dump().items():
        setattr(db_championship, field, value)

    db.commit()
    db.refresh(db_championship)
    return db_championship

@app.delete("/championships/{championship_id}", response_model=ChampionshipResponse)
def delete_championship(championship_id: int, db: Session = Depends(get_db)):
    db_championship = db.query(Championship).filter(Championship.id == championship_id).first()
    if db_championship is None:
        raise HTTPException(status_code=404, detail="Championship not found")

    db.delete(db_championship)
    db.commit()
    return db_championship


                                #*** Participance CRUD ***#

@app.post("/participances/", response_model=ParticipanceResponse)
def create_participance(participance: ParticipanceCreate, db: Session = Depends(get_db)):
    db_participance = Participance(**participance.model_dump())
    db.add(db_participance)
    db.commit()
    db.refresh(db_participance)
    return db_participance

@app.get("/participances/{participance_id}", response_model=ParticipanceResponse)
def read_participance(participance_id: int, db: Session = Depends(get_db)):
    db_participance = db.query(Participance).filter(Participance.id == participance_id).first()
    if db_participance is None:
        raise HTTPException(status_code=404, detail="Participance not found")
    return db_participance

@app.get("/participances/", response_model=List[ParticipanceResponse])
def get_all_participances(db: Session = Depends(get_db)):
    participances = db.query(Participance).all()
    return participances

@app.put("/participances/{participance_id}", response_model=ParticipanceResponse)
def update_participance(participance_id: int, updated_participance: ParticipanceCreate, db: Session = Depends(get_db)):
    db_participance = db.query(Participance).filter(Participance.id == participance_id).first()
    if db_participance is None:
        raise HTTPException(status_code=404, detail="Participance not found")

    for field, value in updated_participance.model_dump().items():
        setattr(db_participance, field, value)

    db.commit()
    db.refresh(db_participance)
    return db_participance

@app.delete("/participances/{participance_id}", response_model=ParticipanceResponse)
def delete_participance(participance_id: int, db: Session = Depends(get_db)):
    db_participance = db.query(Participance).filter(Participance.id == participance_id).first()
    if db_participance is None:
        raise HTTPException(status_code=404, detail="Participance not found")

    db.delete(db_participance)
    db.commit()
    return db_participance
uvicorn.run(app, host="127.0.0.1", port=8000)

