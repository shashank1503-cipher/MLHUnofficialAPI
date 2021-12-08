import pymongo
client = pymongo.MongoClient("mongodb+srv://shashank1503:10july1971@cluster0.plg8d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
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
def fetchFromDb(query):
    x = events.find(query,{'_id':False})
    objects = []
    for i in x:
        objects.append(i)
    return objects

