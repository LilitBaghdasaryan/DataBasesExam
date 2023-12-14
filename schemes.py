from pydantic import BaseModel
from datetime import date

from pydantic import BaseModel

class ParticipanceCreate(BaseModel):
    start_num: int
    place_won: int
    player_id: int
    championship_id: int

class ParticipanceResponse(ParticipanceCreate):
    id: int

class ChessPlayerCreate(BaseModel):
    surname: str
    country: str
    rating: int
    title: str

class ChessPlayerResponse(ChessPlayerCreate):
    id: int

class ChampionshipCreate(BaseModel):
    title: str
    country: str
    city: str
    date: date
    qualification_level: str

    def model_dump(self):
        return {
            "title": self.title,
            "country": self.country,
            "city": self.city,
            "date": str(self.date),
            "qualification_level": self.qualification_level
        }

class ChampionshipResponse(ChampionshipCreate):
    id: int


