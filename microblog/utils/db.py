from pymongo import MongoClient
from ..models.entry import entry_schema
from dotenv import load_dotenv
from os import getenv
from .flask_mongo import PymongoDB_Collection

load_dotenv()

MONGO_URI = getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tz_aware=True)
microblog_db = PymongoDB_Collection(client.microblog)
microblog_db.entries = microblog_db.collection_doc("entries", entry_schema)