import pymongo
import json
from tqdm import tqdm
from time import sleep


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["bellamassa"]
collection = database["enderecos"]

with open("enderecos.json") as file:
  enderecos = json.load(file)
  for i in tqdm(enderecos, total=127353):
    insert = collection.insert_one(i)