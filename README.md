# 💼 Employee Salary Prediction System

An end-to-end Machine Learning application that predicts an employee's estimated annual salary based on professional, educational, technical, and employment-related attributes.

The project combines a trained **HistGradientBoostingRegressor** machine learning model with a **Flask REST API** and an interactive **Streamlit frontend**. Users can enter employee details through the web interface and receive an estimated annual salary prediction in real time.

## 🚀 Live Application

**Try the live Employee Salary Prediction System here:**

👉 https://emplyee-salary-prediction-system.streamlit.app/

> **Note:** The application backend is hosted on a free cloud service and may become idle after a period of inactivity. If the application has been inactive, the first prediction request may take a little longer while the backend service wakes up.

---

## 📌 Project Overview

Salary prediction can help employees, job seekers, recruiters, and organizations estimate compensation based on various professional characteristics.

This project demonstrates a complete machine learning workflow:

1. Data loading and exploration
2. Data preprocessing
3. Categorical feature encoding
4. Feature preparation and alignment
5. Machine learning model training
6. Model evaluation and comparison
7. Model serialization using Joblib
8. Flask REST API development
9. Streamlit frontend development
10. Cloud deployment

The application accepts employee information such as job title, experience, education, skills, industry, company size, location, remote work status, and certifications, and uses the trained machine learning model to estimate annual salary.

---

## ✨ Features

* 💰 Predicts estimated annual employee salary
* 🤖 Machine learning-based salary prediction
* 📊 Uses `HistGradientBoostingRegressor`
* 🌐 Interactive Streamlit web interface
* 🔌 Flask REST API for model inference
* 🧹 Data preprocessing and categorical feature encoding
* 🔄 Feature alignment using saved training columns
* 💾 Model persistence using Joblib
* ☁️ Cloud deployment for public access
* 📱 User-friendly input controls
* ⚡ Lightweight trained model suitable for deployment
* 🔁 API request handling with timeout and retry support
* 🛡️ User-friendly error handling for temporary backend availability issues

---

## 🧠 Machine Learning Model

Several regression approaches were considered during the model development process, including **Random Forest Regression** and **HistGradientBoostingRegressor**.

After comparing model performance and deployment considerations, **HistGradientBoostingRegressor** was selected as the final model.

### Why HistGradientBoostingRegressor?

`HistGradientBoostingRegressor` was selected because it provided an excellent balance between:

* High predictive performance
* Low model file size
* Faster deployment
* Lower storage requirements
* Efficient inference
* Suitability for cloud deployment

The model achieved a high R² score while producing a significantly smaller serialized model file compared with the Random Forest model.

This was particularly important because the initial Random Forest model produced a very large Joblib file that exceeded GitHub's individual file size limit. The HistGradientBoosting model reduced the model size substantially while also improving prediction performance.

---

## 📊 Model Performance

The final `HistGradientBoostingRegressor` model achieved the following results on the test dataset:

| Metric                             |        Result |
| ---------------------------------- | ------------: |
| **Mean Absolute Error (MAE)**      |      4,199.52 |
| **Mean Squared Error (MSE)**       | 27,710,022.02 |
| **Root Mean Squared Error (RMSE)** |      5,264.03 |
| **R² Score**                       |        0.9801 |

### Performance Interpretation

The R² score of approximately **0.98** indicates that the model explains around **98% of the variation in salary values** in the test dataset.

The MAE of approximately **$4,199.52** means that, on average, the model's salary predictions differ from the actual salary values by approximately $4,200.

The RMSE of approximately **$5,264.03** provides an additional measure of prediction error and indicates that the model performs well for the given dataset.

Overall, the model demonstrates strong predictive performance for this salary prediction task.

> Model performance may vary depending on the training/test split, dataset characteristics, preprocessing, and future data.

---

## 📋 Dataset Features

The model uses the following employee and job-related attributes:

| Feature            | Description                                 |
| ------------------ | ------------------------------------------- |
| `job_title`        | Employee's job title or professional role   |
| `experience_years` | Number of years of professional experience  |
| `education_level`  | Highest level of education                  |
| `skills_count`     | Number of relevant professional skills      |
| `industry`         | Industry in which the employee works        |
| `company_size`     | Size category of the employing organization |
| `location`         | Geographic location of employment           |
| `remote_work`      | Whether the employee works remotely         |
| `certifications`   | Number of professional certifications       |

### Target Variable

The target variable is:

```text
salary
```

The model predicts the estimated annual salary based on the provided employee attributes.

---

## 🔄 Machine Learning Workflow

The overall machine learning workflow is:

```text
Dataset
    │
    ▼
Data Exploration
    │
    ▼
Feature Selection
    │
    ▼
Separate Features and Target
    │
    ▼
Categorical Feature Encoding
    │
    ▼
Train/Test Split
    │
    ▼
Train Regression Models
    │
    ├───────────────┐
    ▼               ▼
Random Forest   HistGradientBoosting
    │               │
    └───────┬───────┘
            ▼
     Model Comparison
            │
            ▼
  Select Best Performing Model
            │
            ▼
 HistGradientBoostingRegressor
            │
            ▼
 Save Model using Joblib
            │
            ▼
      Flask REST API
            │
            ▼
    Streamlit Frontend
            │
            ▼
   Salary Prediction
```

---

## 🌐 Application Architecture

The application consists of two main components:

### 1. Streamlit Frontend

The Streamlit application provides an interactive interface where users enter employee information.

The frontend sends the input data to the Flask API using an HTTP POST request.

### 2. Flask Backend

The Flask application acts as a REST API that:

1. Receives employee data in JSON format
2. Converts the input into a Pandas DataFrame
3. Applies the required categorical encoding
4. Aligns the input features with the training columns
5. Loads the trained machine learning model
6. Generates a salary prediction
7. Returns the prediction as a JSON response

The architecture can be represented as:

```text
                   User
                     │
                     ▼
          Streamlit Web Interface
                     │
                     │ HTTP POST /predict
                     ▼
              Flask REST API
                     │
                     ▼
          Data Preprocessing
                     │
                     ▼
       Feature Column Alignment
                     │
                     ▼
   HistGradientBoostingRegressor
                     │
                     ▼
           Salary Prediction
                     │
                     ▼
          Flask JSON Response
                     │
                     ▼
         Streamlit Result Display
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* HistGradientBoostingRegressor

### Backend

* Flask
* Flask-CORS

### Frontend

* Streamlit

### Model Persistence

* Joblib

### Deployment

* Streamlit Community Cloud
* Render

### Version Control

* Git
* GitHub

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Employee_Salary_Prediction
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application Locally

The application consists of a Flask backend and a Streamlit frontend.

### Step 1: Start the Flask API

From the project root directory, run:

```bash
python app.py
```

The Flask API will run locally on:

```text
http://127.0.0.1:5000
```

The prediction endpoint is:

```text
POST /predict
```

### Step 2: Start the Streamlit Frontend

Open another terminal and run:

```bash
streamlit run streamlit_app/app.py
```

The Streamlit application will open in your browser.

The frontend communicates with the Flask backend to generate salary predictions.

---

## 🔌 API Request Example

The Flask API accepts employee information in JSON format.

Example request:

```json
{
    "job_title": "Data Scientist",
    "experience_years": 8,
    "education_level": "Master",
    "skills_count": 12,
    "industry": "Finance",
    "company_size": "Enterprise",
    "location": "Germany",
    "remote_work": "Yes",
    "certifications": 4
}
```

The API processes the request and returns an estimated salary prediction.

Example response:

```json
{
    "predicted_salary": 145000.0
}
```

The actual prediction will vary based on the trained model and input values.

---

## 📁 Project Structure

```text
Employee_Salary_Prediction/
│
├── dataset/
│   └── salary_prediction_dataset.csv
│
├── models/
│   ├── salary_prediction_model.joblib
│   └── train_columns.joblib
│
├── notebooks/
│   └── eda.ipynb
│
├── streamlit_app/
│   └── app.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Descriptions

| File/Directory     | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `dataset/`         | Contains the salary prediction dataset                  |
| `models/`          | Contains the trained model and training feature columns |
| `notebooks/`       | Contains exploratory data analysis and experimentation  |
| `streamlit_app/`   | Contains the Streamlit frontend                         |
| `app.py`           | Flask REST API backend                                  |
| `requirements.txt` | Python project dependencies                             |
| `README.md`        | Project documentation                                   |
| `.gitignore`       | Specifies files excluded from Git tracking              |

---

## 💾 Model Serialization

The trained machine learning model is saved using Joblib:

```text
models/salary_prediction_model.joblib
```

The exact feature columns used during model training are also saved:

```text
models/train_columns.joblib
```

During prediction, the Flask API uses the saved training columns to ensure that the input features match the feature structure expected by the trained model.

This helps prevent feature mismatch errors between the training and prediction stages.

---

## ☁️ Deployment

The application is deployed using a two-part architecture.

### Streamlit Frontend

The interactive user interface is deployed using Streamlit Community Cloud.

### Flask Backend

The Flask REST API is deployed separately as a web service.

The Streamlit frontend sends prediction requests to the deployed Flask backend through the `/predict` API endpoint.

This separation allows the machine learning API and user interface to operate independently.

---

## ⚠️ Deployment Considerations

The backend is hosted using a free cloud hosting service that may put the service into an idle or sleeping state after a period of inactivity.

As a result:

* The first request after inactivity may take longer.
* The backend may need a few moments to wake up.
* A request may occasionally require another attempt.
* The Streamlit frontend includes user-friendly handling for temporary connection issues.

This behavior is related to the hosting environment and does not indicate a problem with the machine learning model itself.

---

## 🔮 Future Improvements

Possible future enhancements include:

* Adding additional salary-related features
* Improving model hyperparameter tuning
* Testing additional regression algorithms
* Adding model explainability using SHAP
* Displaying salary ranges instead of a single prediction
* Adding confidence or uncertainty estimates
* Adding visual salary comparisons
* Improving API authentication and security
* Adding automated model retraining
* Implementing CI/CD deployment workflows
* Adding a database for storing prediction history
* Improving frontend design and user experience

---

## 🎯 Learning Outcomes

This project provided practical experience in:

* Exploratory Data Analysis
* Data preprocessing
* Categorical feature encoding
* Regression model training
* Model evaluation
* Comparing machine learning algorithms
* Model serialization using Joblib
* REST API development with Flask
* Frontend development with Streamlit
* Connecting frontend and backend applications
* Git and GitHub version control
* Cloud deployment
* Handling deployment and API connectivity issues

---

## 👨‍💻 Author

**Rafaqat Muneer**

Developed as an end-to-end Machine Learning capstone project demonstrating the complete workflow from data preprocessing and model development to API integration, interactive frontend development, and cloud deployment.

---

## 📄 License

This project is developed for educational and portfolio purposes.
