import os
from flask import Flask, render_template, request, redirect, url_for
from mongo import get_reviews, add_review, edit_review, delete_review  # Import functions from mongo.py

# Load environment variables if available
if os.path.exists("env.py"):
    import env

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
