import pymongo
import os
client = pymongo.MongoClient(f'mongodb+srv://{os.environ.get("password")}@cluster0.plg8d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.HackathonEvents
events = db.MLH
def addToDB(event):
    try:
        events.insert_one(event)
        print("Added")
    except:
        print("Error")
def fetchCountFromDb(event):
    x = events.count_documents(event)
    return x
def delete(query):
    try:
        events.delete_one(query)
        print("Deleted")
    except:
        print("Error")
def fetchFromDb(query):
    x = events.find(query,{'_id':False})
    objects = []
    for i in x:
        objects.append(i)
    return objects

