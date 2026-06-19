# 🩺 Diabetes Prediction Using Machine Learning & AI

## 📌 Overview

This project is a Machine Learning and AI-powered web application that predicts whether a person is likely to have diabetes based on various health parameters. The model is trained on the Pima Indians Diabetes Dataset and deployed using Streamlit for an interactive user experience.

The application allows users to enter medical and personal health information such as glucose level, blood pressure, BMI, insulin level, and age to receive a diabetes risk prediction.

---

## 🚀 Features

* Interactive Streamlit web application
* User-friendly interface for health data input
* Automatic BMI calculation from height and weight
* Real-time diabetes prediction
* Data preprocessing using StandardScaler
* Trained Support Vector Machine (SVM) model
* Model deployment using Streamlit Cloud

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## 📊 Dataset

**Source:** Pima Indians Diabetes Database (Kaggle)

### Features Used

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

### Target Variable

* **0** → Non-Diabetic
* **1** → Diabetic

---

## ⚙️ Machine Learning Workflow

1. Data Collection and Analysis
2. Data Preprocessing
3. Feature Scaling using StandardScaler
4. Train-Test Split
5. Model Training using Support Vector Machine (SVM)
6. Model Evaluation using Accuracy Score
7. Model Serialization using Joblib
8. Streamlit Web App Development
9. Cloud Deployment

---

## 📈 Model Performance

| Metric            | Score |
| ----------------- | ----- |
| Training Accuracy | ~82%  |
| Testing Accuracy  | ~72%  |

*Performance may vary slightly depending on train-test split and model parameters.*

---

## 🖥️ How It Works

1. User enters health-related information.
2. Input data is converted into a DataFrame.
3. The same scaler used during training standardizes the input.
4. The trained SVM model predicts the outcome.
5. The application displays whether the person is likely diabetic or non-diabetic.

---

## 📂 Project Structure

```text
Diabetes_prediction-project/
│
├── app.py
├── SVM_diabetes.pkl
├── diabetes_scaler.pkl
├── diabetes_columns.pkl
├── requirements.txt
├── diabetes.csv
└── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Future Improvements

* Probability-based risk score
* Enhanced UI/UX design
* Additional health insights and recommendations
* Support for more advanced diabetes prediction models

---

## 👩‍💻 Author

**Minal Duggal**

Machine Learning & AI Enthusiast passionate about building practical AI solutions and deploying end-to-end ML applications.
