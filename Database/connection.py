from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("MongoDbUrl")

connectionstring = MongoClient(url)

Database=connectionstring["student123"]

collection=Database["allstudents1"]