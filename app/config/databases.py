from pymongo.mongo_client import MongoClient
import os

DB_USER=os.environ["DB_USER"]
DB_PASSWORD=os.environ["DB_PASSWORD"]
DB_HOST=os.environ["DB_HOST"]
DB_PORT=os.environ["DB_PORT"]
DB_DATABASE=os.environ["DB_DATABASE"]

uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_DATABASE}.gercpam.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.myduoisok
