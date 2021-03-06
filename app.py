# Import dependencies
from flask import Flask, render_template, request
import numpy as np
import joblib

# Flask Setup
app = Flask(__name__)

# Flask Routes

# Create a welcome page route
@app.route("/")
def welcome():
    return render_template(
        "index.html"
    )

# ETL page
@app.route("/etl")
def etl():
    return render_template(
        "etl.html"
    )

# Data exploration page
@app.route("/data-exploration")
def data_exploration():
    return render_template(
        "dataexploration.html"
    )


@app.route("/data-analysis")
def data_analysis():
    return render_template(
        "data_analysis.html"
    )

# Pages for each model
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

# Prediction page
@app.route("/predict-default")
def predict_default():
    return render_template(
        "predictdefault.html"
    )

# Load the model
model_filename = 'saved_models/final_model_trained.joblib'
model = joblib.load(model_filename)

# Load the scaler
scaler_filename = 'scaler.joblib'
scaler = joblib.load(scaler_filename)

@app.route("/predict-default", methods=["POST"])
def model_prediction():
    try:
        features = [float(x) for x in request.form.values()]

        final_features = [np.array(features)]

        final_features_scaled = scaler.transform(final_features)

        prediction = model.predict(final_features_scaled)

        if prediction[0] == 1:
            final_prediction = 'Based on the Random Forest model, you will default'
        else:
            final_prediction = 'Based on the Random Forest model, you will not default'
    
        return render_template("predictdefault.html", final_prediction=final_prediction)
    except:
        error_message = 'Please submit a valid form'
        return render_template("predictdefault.html", error_message=error_message)


if __name__ == '__main__':
   app.run(debug=True)