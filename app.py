import os
import pymongo
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
    # Fetch all documents (game reviews) from the collection
    documents = coll.find()
    reviews = [doc for doc in documents]  # Convert cursor to list
    return render_template('index.html', reviews=reviews)

# Route to handle form submission for adding new reviews
@app.route('/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        # Get form data
        game = request.form.get('game')
        review = request.form.get('review')
        rating = request.form.get('rating')

        # Create a new review document with correct fields
        new_review = {
            'game': game,      # Use 'game' instead of 'title'
            'review': review,  # Use 'review' instead of 'comment'
            'rating': rating   # Use 'rating' as is
        }

        # Insert the new review into the MongoDB collection
        coll.insert_one(new_review)

        # Redirect back to the home page
        return redirect(url_for('index'))

    return render_template('add_review.html')

if __name__ == '__main__':
    app.run(debug=True)
