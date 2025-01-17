import os
import pymongo
from bson import ObjectId  # Import ObjectId from bson
from flask import Flask, render_template, request, redirect, url_for

# Load environment variables if available
if os.path.exists("env.py"):
    import env

# MongoDB connection details
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

# Connect to MongoDB and get the collection
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

# Initialize Flask app
app = Flask(__name__)

# Set up static and template folders
app.static_folder = 'static'
app.template_folder = 'templates'

# Route to show game reviews
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    reviews = get_reviews(search_query)  # Use the get_reviews function from mongo.py
    return render_template('index.html', reviews=reviews, search_query=search_query)

# Route to handle form submission for adding new reviews
@app.route('/add', methods=['GET', 'POST'])
def add_review_route():
    if request.method == 'POST':
        game = request.form.get('game')
        review = request.form.get('review')
        rating = request.form.get('rating')
        add_review(game, review, rating)  # Use the add_review function from mongo.py
        return redirect(url_for('index'))
    return render_template('add_review.html')

# Route to handle editing a review
@app.route('/edit/<review_id>', methods=['GET', 'POST'])
def edit_review_route(review_id):
    if request.method == 'POST':
        game = request.form.get('game')
        review = request.form.get('review')
        rating = request.form.get('rating')
        edit_review(review_id, game, review, rating)  # Use the edit_review function from mongo.py
        return redirect(url_for('index'))
    
    # Fetch the review details from MongoDB before rendering the edit form
    reviews = get_reviews()
    review = next((r for r in reviews if str(r['_id']) == review_id), None)
    if review:
        return render_template('edit_review.html', review=review)
    return redirect(url_for('index'))

# Route to handle deleting a review
@app.route('/delete/<review_id>', methods=['GET'])
def delete_review_route(review_id):
    delete_review(review_id)  # Use the delete_review function from mongo.py
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
