import streamlit as st
import requests
import traceback
import time
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Employee Salary Prediction")
st.write("Enter the employee details below to predict the estimated annual salary.")

# ==========================
# Personal Information
# ==========================
st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    experience_years = st.slider(
        "Experience (Years)",
        min_value=0,
        max_value=20,
        value=5
    )

with col2:
    education_level = st.selectbox(
        "Education Level",
        [
            "Bachelor",
            "PhD",
            "High School",
            "Diploma",
            "Master"
        ]
    )

# ==========================
# Job Information
# ==========================
st.subheader("💻 Job Information")

col1, col2 = st.columns(2)

with col1:
    job_title = st.selectbox(
        "Job Title",
        [
            "AI Engineer",
            "Data Analyst",
            "Frontend Developer",
            "Business Analyst",
            "Product Manager",
            "Backend Developer",
            "Machine Learning Engineer",
            "DevOps Engineer",
            "Software Engineer",
            "Cybersecurity Analyst",
            "Data Scientist",
            "Cloud Engineer"
        ]
    )

with col2:
    industry = st.selectbox(
        "Industry",
        [
            "Healthcare",
            "Telecom",
            "Media",
            "Retail",
            "Manufacturing",
            "Education",
            "Finance",
            "Technology",
            "Consulting",
            "Government"
        ]
    )

# ==========================
# Company Information
# ==========================
st.subheader("🏢 Company Information")

col1, col2 = st.columns(2)

with col1:
    company_size = st.selectbox(
        "Company Size",
        [
            "Medium",
            "Small",
            "Large",
            "Enterprise",
            "Startup"
        ]
    )

with col2:
    location = st.selectbox(
        "Location",
        [
            "India",
            "Australia",
            "Singapore",
            "Canada",
            "Sweden",
            "USA",
            "Netherlands",
            "Remote",
            "Germany",
            "UK"
        ]
    )

remote_work = st.selectbox(
    "Remote Work",
    [
        "Hybrid",
        "No",
        "Yes"
    ]
)

# ==========================
# Skills
# ==========================
st.subheader("🛠 Skills")

col1, col2 = st.columns(2)

with col1:
    skills_count = st.number_input(
        "Skills Count",
        min_value=0,
        max_value=19,
        value=5,
        step=1
    )

with col2:
    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=5,
        value=1,
        step=1
    )

# ==========================
# Buttons
# ==========================
col1, col2 = st.columns(2)

with col1:
    predict = st.button(
        "💰 Predict Salary",
        use_container_width=True
    )

with col2:
    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

# Reset App
if reset:
    st.rerun()

# ==========================
# Prediction
# ==========================

if predict:

    payload = {
        "job_title": job_title,
        "experience_years": experience_years,
        "education_level": education_level,
        "skills_count": skills_count,
        "industry": industry,
        "company_size": company_size,
        "location": location,
        "remote_work": remote_work,
        "certifications": certifications
    }

    API_URL = "https://employee-salary-prediction-t342.onrender.com"

    max_retries = 3
    result = None

    try:

        # Try the prediction request up to 3 times
        for attempt in range(max_retries):

            try:

                # Display a friendly loading message
                if attempt == 0:
                    message = (
                        "🔄 Connecting to the prediction service... "
                        "Please wait."
                    )
                else:
                    message = (
                        f"🔄 Retrying prediction "
                        f"({attempt + 1}/{max_retries})..."
                    )

                # Show spinner while waiting for API response
                with st.spinner(message):

                    response = requests.post(
                        API_URL,
                        json=payload,
                        timeout=60
                    )

                # If prediction is successful
                if response.status_code == 200:

                    result = response.json()
                    break

                # Handle server-side errors (500+)
                elif response.status_code >= 500:

                    if attempt < max_retries - 1:
                        time.sleep(5)
                        continue

                    else:
                        st.warning(
                            "⚠️ The prediction service is temporarily "
                            "unavailable. Please try again in a moment."
                        )

                # Handle other HTTP errors
                else:

                    st.warning(
                        "⚠️ Unable to process your prediction. "
                        "Please check your inputs and try again."
                    )
                    break

            # Handle request timeout
            except requests.exceptions.Timeout:

                if attempt < max_retries - 1:

                    time.sleep(5)
                    continue

                else:

                    st.warning(
                        "⏳ The prediction service is taking longer "
                        "than expected. Please try again in a moment."
                    )

            # Handle connection errors
            except requests.exceptions.ConnectionError:

                if attempt < max_retries - 1:

                    time.sleep(5)
                    continue

                else:

                    st.warning(
                        "🔌 The prediction service is currently "
                        "unavailable. Please wait a few seconds "
                        "and try again."
                    )

            # Handle other request errors
            except requests.exceptions.RequestException:

                if attempt < max_retries - 1:

                    time.sleep(5)
                    continue

                else:

                    st.warning(
                        "⚠️ We couldn't connect to the prediction "
                        "service. Please try again shortly."
                    )

        # ==========================================
        # Display Prediction Result
        # ==========================================

        if result:

            prediction = result["predicted_salary"]

            st.success("✅ Prediction Successful!")

            st.metric(
                label="💵 Estimated Annual Salary",
                value=f"${prediction:,.0f}"
            )

        # ==========================================
        # Show Try Again Button if Prediction Fails
        # ==========================================

        elif result is None:

            if st.button(
                "🔄 Try Again",
                key="retry_prediction"
            ):
                st.rerun()

    # ==========================================
    # Final Safety Net
    # ==========================================

    except Exception:

        st.warning(
            "⚠️ Something went wrong while processing your prediction. "
            "Please try again in a few moments."
        )

# ==========================
# About Model
# ==========================
with st.expander("ℹ About the Model"):

    st.markdown("""
**Model:** Random Forest Regressor

**Machine Learning Library:** Scikit-learn

**Prediction Target:** Annual Employee Salary

### Input Features
- Job Title
- Experience Years
- Education Level
- Skills Count
- Industry
- Company Size
- Location
- Remote Work
- Certifications

### Evaluation Metrics
- **R² Score:** 0.9801
- **MAE:** 4199.52
- **RMSE:** 5264.03

This application predicts an employee's estimated annual salary based on professional qualifications and job-related attributes.
""")