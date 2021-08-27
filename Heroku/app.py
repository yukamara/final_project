#import Flask
from joblib import load
from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template
# create an instance of Flask
app = Flask(__name__)

# load the pipeline object
#pipeline = load("model_name.joblib")


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
