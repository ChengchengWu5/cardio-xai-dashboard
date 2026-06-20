Cardiovascular Risk Prediction and Explainable AI (XAI) Dashboard

Project Overview
This project demonstrates the development of an Explainable Artificial Intelligence (XAI) framework for cardiovascular disease (CVD) risk prediction using the Cardiovascular Disease Dataset from Kaggle.
The project covers the complete machine learning workflow, including data preparation, feature engineering, model development, performance evaluation, model interpretation, and dashboard deployment. The aim is not only to predict cardiovascular risk but also to provide transparent explanations that help users understand the factors driving each prediction.

Project Objectives
* Develop machine learning models for cardiovascular disease risk prediction.
* Compare model performance using multiple evaluation metrics.
* Apply Explainable AI (XAI) techniques to improve model transparency.
* Generate both global and patient-level explanations of model predictions.
* Build an interactive dashboard for communicating predictions and explanations to different audiences.

Dataset
The project uses the Cardiovascular Disease Dataset (cardio_train.csv) obtained from Kaggle.
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

Machine Learning Models
Three supervised machine learning algorithms were developed and compared:
* Logistic Regression
* Random Forest
* Gradient Boosting
Model Evaluation Metrics
Models were evaluated using:
* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix
The Gradient Boosting model achieved the best overall performance and was selected for explainability analysis and dashboard deployment.

Explainable AI (XAI)
To improve transparency and trustworthiness, SHAP (SHapley Additive exPlanations) was applied to interpret model behaviour at both global and individual levels.
Global Explanations
* Model Feature Importance
* SHAP Global Feature Importance
* SHAP Summary Plot
* SHAP Beeswarm Plot
Local Explanations
* Patient-Level Waterfall Plot
* Individual Risk Factor Analysis
* Prediction Interpretation
These visualisations help users understand how different features contribute to cardiovascular risk predictions.

Interactive Dashboard
The final output is an interactive dashboard built using Dash and Plotly (app.py).
The dashboard allows users to:
* Explore cardiovascular risk predictions
* Investigate model explanations
* Compare feature importance
* Examine patient-specific risk profiles
Intended Audiences
* Patients
* Clinicians
* Healthcare Researchers
* Data Scientists and Machine Learning Practitioners

Technologies Used
* Python 3.10.9
* Pandas
* NumPy
* Scikit-learn
* SHAP
* Plotly
* Dash
* Matplotlib
* Joblib

Running the Dashboard
1. Navigate to the project directory
cd cardio-xai-dashboard
2. Install required packages
pip install pandas numpy scikit-learn shap dash plotly matplotlib joblib
3. Run the dashboard
python app.py
4. Open the dashboard
Open your browser and navigate to:
http://127.0.0.1:8050

Troubleshooting
If joblib, dash, or other packages work in Jupyter Notebook but not in app.py, verify which Python interpreter is being used:
import sys
print(sys.executable)
Example output:
/usr/local/bin/python3.10
Install packages into that specific Python environment:
/usr/local/bin/python3.10 -m pip install joblib dash plotly pandas scikit-learn shap
Test the imports:
/usr/local/bin/python3.10 -c "import joblib, dash, plotly, pandas, sklearn, shap; print('All imports working')"
Then run:
/usr/local/bin/python3.10 app.py

Key Skills Demonstrated
* Machine Learning Classification
* Healthcare Analytics
* Explainable AI (XAI)
* SHAP Interpretation
* Feature Engineering
* Model Evaluation
* Interactive Dashboard Development
* Data Visualisation
* Python Development
