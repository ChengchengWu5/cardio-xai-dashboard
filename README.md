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

#### Run the dashboard using app.py (or app.ipynb if needed)
- To run the app, go to Terminal and find the folder containing app.py and the model file
- Then open the lcoal URL shown in the Termial (for example: http://127.0.0.1:8050)

- In case joblib and dash work in app.ipynb but not in app.py, run the following first:
    - import sys
    - print(sys.executable)
    to print the output, for example: /usr/local/bin/python3.10
- Then use the exact same path to run app.py in the Terminal
    - for example in Mac: cd ~/Desktop/cardio-xai-dashboard/notebooks/usr/local/bin/python3.10 app.py
- Install packages into that exact Python in the Terminal
    - for example in Mac: /usr/local/bin/python3.10 -m pip install joblib dash plotly pandas scikit-learn
- Test imports
    - for example in Mac: /usr/local/bin/python3.10 -c "import joblib, dash, plotly, pandas, sklearn; print('All imports working')
- Then run the app in the Terminal
    - for example in Mac: cd ~/Desktop/cardio-xai-dashboard/notebooks/usr/local/bin/python3.10 app.py
- Finally, open the url
    - for example: http://127.0.0.1:8050/
