import os
import pymongo
from bson import ObjectId  # Import ObjectId from bson

# Load environment variables if available
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "test"
COLLECTION = "reviews"

# MongoDB connection function
def mongo_connect(URL):
    try:
        conn = pymongo.MongoClient(URL)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)

# Connect to MongoDB
def get_collection():
    conn = mongo_connect(MONGO_URI)
    return conn[DATABASE][COLLECTION]

# Get all reviews
def get_reviews(search_query=''):
    coll = get_collection()
    if search_query:
        documents = coll.find({'game': {'$regex': search_query, '$options': 'i'}})  # Case-insensitive search
    else:
        documents = coll.find()
    return [doc for doc in documents]  # Convert cursor to list

# Add a new review
def add_review(game, review, rating):
    coll = get_collection()
    new_review = {
        'game': game,
        'review': review,
        'rating': rating
    }
    coll.insert_one(new_review)

# Edit an existing review
def edit_review(review_id, game, review, rating):
    coll = get_collection()
    updated_review = {
        'game': game,
        'review': review,
        'rating': rating
    }
    coll.update_one({'_id': ObjectId(review_id)}, {'$set': updated_review})

# Delete a review
def delete_review(review_id):
    coll = get_collection()
    coll.delete_one({'_id': ObjectId(review_id)})
