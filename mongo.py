import os 
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "test"
COLLECTION = "reviews"

def mongo_connect(URL):
    try:
        conn = pymongo.MongoClient(URL)
        print("Mongo is connected")
        return conn#
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {""}

documents = coll.find()

for doc in documents:
    print(doc)