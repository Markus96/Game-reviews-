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
    # Fetch all documents (game reviews) from the collection
    documents = coll.find()
    reviews = [doc for doc in documents]  # Convert cursor to list
    return render_template('index.html', reviews=reviews)

# Route to handle form submission for adding new reviews
@app.route('/add', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('game')  # Get the game title
        review = request.form.get('review')  # Get the review comment
        rating = request.form.get('rating')  # Get the rating value

        # Create a new review document
        new_review = {
            'game': title,  # Use the correct variable 'title'
            'review': review,
            'rating': rating
        }

        # Insert the new review into the MongoDB collection
        coll.insert_one(new_review)

        # Redirect back to the home page
        return redirect(url_for('index'))

    return render_template('add_review.html')

# Route to edit a specific review
@app.route('/edit_review/<review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    # Find the review by its ID
    review = coll.find_one({"_id": ObjectId(review_id)})  # Use ObjectId here
    
    if not review:
        return "Review not found", 404

    if request.method == 'POST':  # Fixed indentation
        # Update review with new form data
        title = request.form.get('game')  # Correct variable name here
        review_text = request.form.get('review')
        rating = request.form.get('rating')

        updated_review = {
            'game': title,  # Corrected variable assignment
            'review': review_text,
            'rating': rating  # Removed the extra quote here
        }

        # Update the review in the database
        coll.update_one({"_id": ObjectId(review_id)}, {"$set": updated_review})

        # Redirect to the home page after update
        return redirect(url_for('index'))

    return render_template('edit_review.html', review=review)

# Route to show delete confirmation page
@app.route('/delete_review/<review_id>', methods=['GET', 'POST'])
def delete_review_route(review_id):
    review = coll.find_one({"_id": ObjectId(review_id)})
    if not review:
        return "Review not found", 404
    
    if request.method == 'POST':
        # Delete the review by its ID
        coll.delete_one({"_id": ObjectId(review_id)})
        return redirect(url_for('index'))
    
    return render_template('delete_review.html', review=review)

if __name__ == '__main__':
    app.run(debug=True)
