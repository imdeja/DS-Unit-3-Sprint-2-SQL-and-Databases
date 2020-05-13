import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime
import wget
import json

load_dotenv()
connection_uri = os.getenv("MONGO_URL")


client = pymongo.MongoClient(connection_uri)


db = client.test_database


collection = db.rpg
#path = os.path.join(os.path.dirname(__file__), "..", "module3-nosql-and-document-oriented-databases", "testdata.json")
#with open(path) as f:
    #file_data = json.load(f)

#collection.insert_many(file_data)

result = collection.count_documents({"model":"charactercreator.character"})
print("There are", result, "total characters.")

result2 = collection.count_documents({"model":"charactercreator.cleric"})
print("There are", result2, "clerics.")

result2 = collection.count_documents({"model":"charactercreator.fighter"})
print("There are", result2, "fighters.")

result2 = collection.count_documents({"model":"charactercreator.mage"})
print("There are", result2, "mages.")

result2 = collection.count_documents({"model":"charactercreator.necromancer"})
print("There are", result2, "necromancers.")

result2 = collection.count_documents({"model":"charactercreator.thief"})
print("There are", result2, "thieves.")

items = collection.count_documents({"model":"armory.item"})
print("There are", items, "total items.")

weapons = collection.count_documents({"model":"armory.weapon"})
print("There are", weapons, "items that are weapons.")

nonweapons = items - weapons
print("There are", nonweapons, "items that are not weapons.")


#How was working with MongoDB different from working with
#PostgreSQL? What was easier, and what was harder?"
'''MongoDB was harder to use because we have to learn different commands 
than SQL. It was very frustrating setting it up and not the biggest fan of it 
yet. In the future I will get used to it and probably prefer it but at the moment, 
I have encountered many issues and not able to replicate every thing from SQL db's.
'''