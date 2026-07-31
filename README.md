# Employee Salary Prediction using Random Forest Regression

## Overview

This project is an end-to-end Machine Learning application that predicts an employee's estimated annual salary based on professional and job-related attributes. The application includes model training, a Flask REST API for prediction, and a Streamlit-based user interface.

## Features

- Employee salary prediction using Random Forest Regression
- Interactive Streamlit user interface
- Flask REST API for prediction
- Data preprocessing using Pandas
- Model serialization using Joblib
- Clean and modular project structure

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Streamlit
- Joblib

## Dataset Features

The model uses the following input features:

- Job Title
- Experience Years
- Education Level
- Skills Count
- Industry
- Company Size
- Location
- Remote Work
- Certifications

## Model Performance

| Metric | Value |
|---------|------:|
| R² Score | 0.9602 |
| Mean Absolute Error (MAE) | 5,740.69 |
| Root Mean Squared Error (RMSE) | 7,441.02 |

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Employee_Salary_Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the Flask API

```bash
python app.py
```

### 2. Launch the Streamlit Frontend

```bash
streamlit run streamlit_app/app.py
```

## Project Workflow

1. Data Collection and Exploration
2. Data Preprocessing
3. Model Training using Random Forest Regressor
4. Model Evaluation
5. Save Model using Joblib
6. Flask API Development
7. Streamlit UI Development

## Project Structure

```text
Employee_Salary_Prediction/
│
├── dataset/
├── models/
│   └── salary_prediction_model.joblib
├── streamlit_app/
│   └── app.py
├── app.py
├── requirements.txt
└── README.md
```

## Author

Developed as an end-to-end Machine Learning capstone project using Python, Flask, Streamlit, and Scikit-learn.
