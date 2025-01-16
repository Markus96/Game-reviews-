import os
import pymongo
from bson import ObjectId  # Import ObjectId from bson
from flask import Flask, render_template, request, redirect, url_for

# Load environment variables if available
if os.path.exists("env.py"):
    import env

# MongoDB URI and Database setup
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "test"
COLLECTION = "reviews"

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection function
def mongo_connect(URL):
    try:
        conn = pymongo.MongoClient(URL)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s" % e)

# Connect to MongoDB
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]

# Route to show game reviews
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    if search_query:
        documents = coll.find({'title': {'$regex': search_query, '$options': 'i'}})  # Case-insensitive search
    else:
        documents = coll.find()
    
    reviews = [doc for doc in documents]  # Convert cursor to list
    return render_template('index.html', reviews=reviews, search_query=search_query)

# Route to handle form submission for adding new reviews
@app.route('/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        game = request.form.get('game')
        review = request.form.get('review')
        rating = request.form.get('rating')

        new_review = {
            'game': game,
            'review': review,
            'rating': rating
        }

        coll.insert_one(new_review)

        return redirect(url_for('index'))

    return render_template('add_review.html')

# Route to handle editing a review
@app.route('/edit/<review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    review = coll.find_one({'_id': ObjectId(review_id)})  # Use ObjectId for querying
    if not review:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('game')
        comment = request.form.get('review')
        rating = request.form.get('rating')

        updated_review = {
            'game': title,
            'review': review,
            'rating': rating
        }
        
        coll.update_one({'_id': ObjectId(review_id)}, {'$set': updated_review})  # Use ObjectId for updating

        return redirect(url_for('index'))

    return render_template('edit_review.html', review=review)

# Route to handle deleting a review
@app.route('/delete/<review_id>', methods=['GET'])
def delete_review(review_id):
    coll.delete_one({'_id': ObjectId(review_id)})  # Use ObjectId for deletion
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
