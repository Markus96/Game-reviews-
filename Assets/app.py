from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reviews = db.relationship('Review', backref='game', lazy=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('game_detail.html', game=game)

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_game = Game(title=title, description=description)
        try:
            db.session.add(new_game)
            db.session.commit()
            flash('Game added successfully!', 'success')
            return redirect(url_for('index'))
        except:
            flash('Error adding game. Please try again.', 'danger')
    return render_template('add_game.html')

@app.route('/add_review/<int:game_id>', methods=['GET', 'POST'])
def add_review(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == 'POST':
        username = request.form['username']
        rating = request.form['rating']
        comment = request.form['comment']
        new_review = Review(username=username, rating=rating, comment=comment, game=game)
        try:
            db.session.add(new_review)
            db.session.commit()
            flash('Review added successfully!', 'success')
            return redirect(url_for('game_detail', game_id=game_id))
        except:
            flash('Error adding review. Please try again.', 'danger')
    return render_template('add_review.html', game=game)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)