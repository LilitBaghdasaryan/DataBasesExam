from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, ChessPlayer, Championship
from schemes import ChessPlayerCreate, ChampionshipCreate, ParticipanceCreate
from init import DATABASE_URI as db_url
from helper_funcs import random_date
import requests
import json
import random

    
DATABASE_URL = db_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



BASE_URL = "http://127.0.0.1:8000"  # Replace with your FastAPI server URL

def create_chess_player(player: ChessPlayerCreate):
    response = requests.post(f"{BASE_URL}/chess_players/", json=player.model_dump())
    return response.json()

def create_championship(championship: ChampionshipCreate):
    response = requests.post(f"{BASE_URL}/championships/", json=championship.model_dump())
    return response.json()

def create_participance(participance: ParticipanceCreate):
    response = requests.post(f"{BASE_URL}/participances/", json=participance.model_dump())
    return response.json()


json_file_path = "C:\\Users\\Asus\\Desktop\\databaseExam\\DataBasesExam\\data.json"
with open(json_file_path, "r") as file:
    data_dict = json.load(file)

def stuff_chess_players(num_of_elements):
    for _ in range(num_of_elements):
        surname = random.choice(data_dict["surnames"])
        country = random.choice(data_dict["countries and cities"])[0] # the country name is kept at 0th index 

        unique_random_numbers = random.sample(range(1, 100000), 25000)
        rating = random.choice(unique_random_numbers)
        unique_random_numbers.remove(rating)

        title = random.choice(data_dict["titles"])
        player_to_insert = ChessPlayerCreate(surname=surname, country=country, rating=rating, title=title)
        create_chess_player(player_to_insert)
        

def stuff_championships(num_of_elements):
    for _ in range(num_of_elements):
        title = random.choice(data_dict["championship titles"])

        country_city = random.choice(data_dict["countries and cities"])
        country = country_city[0]
        idx = random.randint(1, 2)
        city = country_city[idx] # cities are kept at 1st and 2nd indexes

        if title[0] == " ":
            title = country + title
        date = random_date()
        qualification_level = random.choice(data_dict["qualification levels"])
        championship_to_insert = ChampionshipCreate(title = title, country = country, city = city, date = date, qualification_level = qualification_level)
        create_championship(championship_to_insert)

def stuff_participance(rating_restriction):   # the num of players must be greater than the num of championships
    players_below_rating = session.query(ChessPlayer).filter(ChessPlayer.rating < rating_restriction).all()
    championships = session.query(Championship).filter(Championship.id < 100).all()
    places_to_win = random.sample(range(1, len(players_below_rating) + 1), len(players_below_rating))
    num_of_player = 1
    for player in players_below_rating:
        start_num = num_of_player
        num_of_player += 1
        place_won = places_to_win[0]
        places_to_win.pop(0)
        championship = random.choice(championships)
        participance_to_insert = ParticipanceCreate(start_num=start_num, place_won=place_won, player_id=player.id, championship_id=championship.id)
        create_participance(participance_to_insert)

stuff_chess_players(7000)
stuff_championships(3000)
stuff_participance(60000) 


