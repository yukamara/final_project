#import Flask
from joblib import load
import numpy as np
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
import pickle
import os
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfTransformer



# create an instance of Flask
app = Flask(__name__)

# load pipeline object
pipeline = load("amazon_reviews.joblib")


# Define a helper function
# def double(x):
#     return x*2

# create route that renders index.html template
@app.route('/')
def home():
    
    # data = {
    #     "first": "Yusufu",
    #     "last": "Kamara",
    #     "number": double(5)
    # }
    return render_template('home.html', data=data)


# Create a route to get reviews and return ratings for the review
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        review = request.form["amazonReview"]

        rating = pipeline.predict([review])

        rating = rating[0]
        
        print(rating)

    return render_template("home.html", name='This review has a {} star rating.'.format(rating))



if __name__ == '__main__':
    app.run(debug=True)

