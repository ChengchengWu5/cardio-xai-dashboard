### Cardiovascular Risk Prediction and Explainable Artificial Intelligence (XAI) Dashboard

This project demonstrates the development of an Explainable Artificial Intelligence (XAI) framework for cardiovascular risk prediction using a publicly available cardiovascular health dataset from Kaggle. The workflow covers the complete machine learning pipeline, including data preparation, feature engineering, model training, performance evaluation, and model interpretation. 

***Project Objectives:***
- Develop machine learning models for cardiovascular disease risk prediction.
- Compare model performance using multiple evaluation metrics.
- Apply explainable AI techniques to improve model transparency.
- Generate both global and patient-specific explanations of predictions.
- Build an interactive dashboard for communicating risk predictions and model explanations to different audiences.

***Dataset:***
The project uses the Cardiovascular Disease Dataset (cardio_train.csv) obtained from Kaggle. The dataset contains demographic, behavioural, and clinical characteristics commonly associated with cardiovascular disease risk, including:
- Age
- Sex
- Height and weight
- Blood pressure
- Cholesterol level
- Glucose level
- Smoking status
- Alcohol intake
- Physical activity
- Cardiovascular disease diagnosis (target variable)

***Three machine learning algorithms are developed and compared:*** 
- Logistic Regression
- Random Forest
- Gradient Boosting

***Model performance is assessed using standard classification metrics, including:***
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion matrices

To improve transparency and trustworthiness, ***SHAP (SHapley Additive exPlanations)*** is used to explain model behaviour at both global and individual levels for the best performing model slected (Gradient Boosting in this case). The XAI component includes:
- Model-based feature importance analysis
- Global feature importance analysis
- SHAP summary plots
- SHAP beeswarm visualisations
- Individual patient waterfall explanations
- Patient-level risk interpretation

The final output is an ***interactive dashboard built with Dash and Plotly (app.py)***, allowing to explore cardiovascular risk predictions and corresponding explanations. The dashboard is designed to support different audiences interested in understanding the factors that influence cardiovascular risk, such as 
- Patients
- Clinicians
- ML researchers 

***Python version used:*** 3.10.9
