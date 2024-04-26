# !/usr/bin/python

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
#specify a database
db = client.rde6mn
# specify a collection
collection = db.lab9

album_1 = {
    "name" : "Zephyr",
    "artist" : "Niki",
    "genre" : "rnb"
}

album_2 = {
    "name" : "Lover",
    "artist" : "Taylor Swift",
    "genre" : "pop"
}

album_3 = {
    "name" : "Pocket Locket",
    "artist" : "Alaina Castillo",
    "genre" : "rnb"
}

album_4 = {
    "name" : "eternal sunshine",
    "artist" : "Ariana Grande",
    "genre" : "rnb"
}

album_5 = {
    "name" : "GUTS",
    "artist" : "Olivia Rodrigo",
    "genre" : "pop"
}

#collection.insert_many([album_1,album_2, album_3, album_4, album_5])
#getAlbums = []
#getAlbums = db.lab9.find({"genre":"rnb"})
#collection.find()

for x in collection.find({"genre":"rnb"}):
  print(x)