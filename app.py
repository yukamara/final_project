#import Flask
from joblib import load
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfTransformer


# create an instance of Flask
app = Flask(__name__)


# load pipeline object
pipeline = load("amazon_reviews.joblib")
model = pickle.load(open('amazon_reviews.pkl', 'rb'))

# Define a helper function
def double(x):
    return x*2

# create route that renders index.html template
@app.route('/')
def home():
    
    data = {
        "first": "Yusufu",
        "last": "Kamara",
        "number": double(5)
    }
    return render_template('home.html', data=data)


# Create a route to get reviews and return ratings for the review
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        review = request.form["amazonReview"]

        rating = pipeline.predict([review])

        rating = [rating[0]]
        
        print(rating[0])
        # output = TfidfTransformer.transform(rating)

    return render_template("home.html", name=rating)

# Create a route to get the start rating for the inputed review
# @app.route("/result", methods=["POST"])
# def result():

#     data = request.get(force=True)
#     rating = pipeline.predict([np.array(list(data.values()))])

#     star_rating = rating[0]

#     print(star_rating)
#     return star_rating
#     # return render_template("home.html", name=star_rating)


if __name__ == '__main__':
    app.run(debug=True)

