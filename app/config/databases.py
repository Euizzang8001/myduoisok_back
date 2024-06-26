import json
import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DB_USER=os.environ["DB_USER"]
DB_PASSWORD=os.environ["DB_PASSWORD"]
DB_HOST=os.environ["DB_HOST"]
DB_PORT=os.environ["DB_PORT"]
DB_DATABASE=os.environ["DB_DATABASE"]

uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@myduoisok.gercpam.mongodb.net/?retryWrites=true&w=majority&appName=myduoisok"


client = MongoClient(uri) 
  
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e: 
    print(e)

db = client.myduoisok


