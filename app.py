from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# intiating Flask app
app = Flask(__name__)

with open("models/salary_prediction_model.joblib", "rb") as f:
    model = joblib.load(f)
with open("models/train_columns.joblib", "rb") as f:
    train_columns = joblib.load(f)

# creating home
@app.route("/")
def home():
    return {"message": "Salary Prediction API"}

# creating prediction endpoint of the API
@app.route("/predict", methods = ["POST"])

def predict():
    # getting json data from front end or postman for testing

    data = request.json
    # Input as pandas dataframe for using get_dummies
    input_df = pd.DataFrame([{
    "job_title": str(data["job_title"]),
    "experience_years": int(data["experience_years"]),
    "education_level": str(data["education_level"]),
    "skills_count": int(data["skills_count"]),
    "industry": str(data["industry"]),
    "company_size": str(data["company_size"]),
    "location": str(data["location"]),
    "remote_work": str(data["remote_work"]),
    "certifications": int(data["certifications"])
    }])
    # input_df = pd.DataFrame([data])

    input_df = pd.get_dummies(input_df)
    # Re-indexing to match the training columns
    input_df = input_df.reindex(columns=train_columns, fill_value=0)

    prediction = model.predict(input_df)

    # Return data to the front end

    return jsonify({
        "predicted_salary": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
