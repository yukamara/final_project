#import Flask
from joblib import load
from flask import Flask, render_template, request, redirect, url_for
import pickle


# create an instance of Flask
app = Flask(__name__)


# load pipeline object
pipeline = load("amazon_reviews.joblib")
model = pickle.load(open('amazon_reviews.pkl', 'rb'))


# create route that renders index.html template
@app.route('/')
def home():
    return render_template('home.html')


# Create a route to get reviews and return ratings for the review
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["amazonReview"]


        review = pipeline.predict(name)

    return render_template("home.html", review=review)


if __name__ == '__main__':
    app.run(debug=True)
