# Import dependencies
from flask import Flask, render_template

# Flask Setup
app = Flask(__name__)

# Flask Routes

#Create a welcome page route
@app.route("/")
def welcome():
    return render_template(
        "index.html"
    )

#Data exploration page
@app.route("/data-exploration")
def data_exploration():
    return render_template(
        "dataexploration.html"
    )

#Pages for each model
@app.route("/models/logreg")
def log_reg():
    return render_template(
        "logreg.html"
    )

@app.route("/models/trees")
def trees():
    return render_template(
        "trees.html"
    )

@app.route("/models/knn")
def knn():
    return render_template(
        "knn.html"
    )

@app.route("/models/svm")
def svm():
    return render_template(
        "svm.html"
    )

@app.route("/models/nn")
def nn():
    return render_template(
        "nn.html"
    )

if __name__ == '__main__':
   app.run(debug=True)