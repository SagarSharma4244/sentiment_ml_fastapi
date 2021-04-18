from fastapi import APIRouter ,File, UploadFile
from pydantic import BaseModel
import os
import nltk
import shutil
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

model = ResNet50(weights='imagenet')


UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

nltk.download('vader_lexicon')
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



@router.post('/image-recogination-renet-50')
def fileUpload(images_file: UploadFile = File(...)):
    print(os.getcwd())
    print(images_file.file)
    target = os.path.join(os.getcwd(), 'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    filename = images_file.filename
    destination = "/".join([target, filename])
    with open(destination, "wb+") as file_object:
        shutil.copyfileobj(images_file.file, file_object)
    img = image.load_img(destination, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    final = {}
    data = decode_predictions(preds, top=3)[0]
    for xx in data:
        final[str(xx[1])] = {"name": str(xx[1]), "percentage": str(xx[2])}
    print('Predicted:', final)
    return {"data": final}
