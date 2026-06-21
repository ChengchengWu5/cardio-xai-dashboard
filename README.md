# Cardiovascular Disease Risk Prediction and Explainable AI (XAI) Dashboard

## Overview

This project demonstrates the development of an Explainable AI framework for cardiovascular disease risk prediction using a publicly available health dataset from Kaggle.

It covers a machine learning workflow, including data cleaning and preparation, feature engineering, model development, performance evaluation, model interpretation, and dashboard building. The aim is not only to predict cardiovascular disease risk but also to provide transparent explanations that help users understand the factors driving each prediction.

---

## Project Objectives

* Develop machine learning models for cardiovascular disease risk prediction
* Compare model performance using multiple evaluation metrics
* Apply Explainable AI (XAI) techniques to improve model transparency
* Generate both global and patient-level explanations of model predictions
* Build an interactive dashboard for communicating predictions and explanations to different audiences

---

## Dataset

The project uses the **Cardiovascular Disease Dataset (`cardio_train.csv`)** obtained from Kaggle.

The dataset contains demographic, behavioural, and clinical variables associated with cardiovascular disease risk, including:

* Age
* Sex
* Height and Weight
* Blood Pressure
* Cholesterol Level
* Glucose Level
* Smoking Status
* Alcohol Consumption
* Physical Activity
* Cardiovascular Disease Diagnosis (Target Variable)

---

## Machine Learning Models

Three supervised machine learning algorithms were developed and compared:

* Logistic Regression
* Random Forest
* Gradient Boosting

### Model Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

The **Gradient Boosting model** achieved the best overall performance and was selected for explainability analysis and dashboard building.

---

## Explainable AI

To improve transparency and trustworthiness, **SHAP (SHapley Additive exPlanations)** was applied to interpret model behaviour at both global and individual levels.

### Global Explanations

* Model-Based Feature Importance
* SHAP Global Feature Importance
* SHAP Summary Plot
* SHAP Beeswarm Plot

### Local Explanations

* Individual Patient Waterfall Plot
* Patient-Level Risk Interpretation

These visualisations help users understand how different features contribute to cardiovascular disease risk predictions.

---

## Interactive Dashboard

The final output is an interactive dashboard built with **Dash** and **Plotly** (`app.py`).

The dashboard enables users to:

* Explore cardiovascular disease risk predictions
* Investigate model explanations
* Compare feature importance
* Examine patient-specific risk profiles

### Intended Audiences

* Patients
* Clinicians
* Machine Learning researchers

---

## Technologies Used

* Python 3.10.9
* Pandas
* NumPy
* Scikit-learn
* SHAP
* Plotly
* Dash
* Matplotlib
* Joblib

---

## Project Structure

```text
cardio-xai-dashboard/
│
├── dashboard_reports/
│   ├── XAI Dashboard - Clinician Explanation.pdf
│   ├── XAI Dashboard - Ethics and Safety.pdf
│   ├── XAI Dashboard - Machine Learning Researcher View.pdf
│   └── XAI Dashboard - Patient-Friendly Explanation.pdf
├── data/
│   └── cardio_train.csv
├── images/
│   ├── gradient_boosting_model_feature_importance.png
│   ├── shap_global_importance.png
│   ├── shap_summary_beeswarm_plot.png
│   └── shap_waterfall_patient_50.png
├── notebooks/
│   ├── app.ipynb
│   ├── app.py
│   └── cardio-xai.ipynb
├── selected_model/
│   └── gradient_boosting_cardio_model.pkl
└── README.md
```

---

## Running the Dashboard

### 1. Clone the repository

```bash
git clone <repository-url>
cd cardio-xai-dashboard
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn shap dash plotly matplotlib joblib
```

### 3. Run the application

```bash
python app.py
```

### 4. Open the dashboard

Navigate to:

```text
http://127.0.0.1:8050
```

---

## Troubleshooting

If `joblib`, `dash`, or other packages work in Jupyter Notebook but not in `app.py`, verify which Python interpreter is being used:

```python
import sys
print(sys.executable)
```

Example output:

```text
/usr/local/bin/python3.10
```

Install packages into that specific environment:

```bash
/usr/local/bin/python3.10 -m pip install joblib dash plotly pandas scikit-learn shap
```

Verify imports:

```bash
/usr/local/bin/python3.10 -c "import joblib, dash, plotly, pandas, sklearn, shap; print('All imports working')"
```

Run the application:

```bash
/usr/local/bin/python3.10 app.py
```
OR run app.ipynb instead

---

## Key Skills Demonstrated

* Machine Learning Classification
* Healthcare Analytics
* Explainable AI (XAI)
* SHAP Model Interpretation
* Feature Engineering
* Model Evaluation
* Interactive Dashboard Development
* Data Visualisation
* Python Development

---

## Future Enhancements

* Compare additional machine learning models (e.g., XGBoost, LightGBM)
* Add patient-friendly explanation views
* Incorporate model fairness and bias assessment
* Support real-time risk prediction using user inputs
* Conduct usability testing with patients, clinicians, and Machine Learning researchers
