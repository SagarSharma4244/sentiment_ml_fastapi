from fastapi import APIRouter
from pydantic import BaseModel
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
router = APIRouter()
class City(BaseModel):
    name:str
    timezone:str

# cities
@router.get('/')
async def get_cities():
    return db


@router.get('/{city_id}')
def get_single_cities():
    return db[city_id]



@router.post('/sentiment-analysis')
def profile(data):
    return {"data": sid.polarity_scores(data)}
