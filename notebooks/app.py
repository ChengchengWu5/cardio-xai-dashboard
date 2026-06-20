# Interactive Explainable Dashboard for Cardiovascular Risk Prediction

'''# In case joblib and dash work in app.ipynb but not in app.py, run the following first:

import sys
print(sys.executable)   # Output: /usr/local/bin/python3.10

# Then use the exact same path to run app.py in the Terminal, for example:
"""cd ~/Desktop/cardio-xai-dashboard/notebooks
/usr/local/bin/python3.10 app.py"""

# Install packages into that exact Python in the Terminal, for example:
"""/usr/local/bin/python3.10 -m pip install joblib dash plotly pandas scikit-learn"""

# Test imports, for example:
"""/usr/local/bin/python3.10 -c "import joblib, dash, plotly, pandas, sklearn; print('All imports working')"""

# Then run the app in the Terminal, for example:
"""cd ~/Desktop/cardio-xai-dashboard/notebooks
/usr/local/bin/python3.10 app.py"""

# Open the url, for example: http://127.0.0.1:8050/

OR run the code using app.ipynb'''


# Import libraries

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output


# Load trained model

model = joblib.load("gradient_boosting_cardio_model.pkl")


# Feature names used during training

features = [
    "Age",
    "Sex",
    "Systolic_BP",
    "Diastolic_BP",
    "Cholesterol",
    "Glucose",
    "Smoking_status",
    "Alcohol_intake",
    "Physical_activity",
    "BMI"
]


# Create Dash app

app = Dash(__name__)

app.title = "Cardiovascular Risk XAI Dashboard"


# Dashboard layout

app.layout = html.Div([

    html.H1("Interactive Explainable Dashboard for Cardiovascular Risk Prediction"),

    html.P(
        "This dashboard predicts cardiovascular disease risk and explains the result "
        "for patients, clinicians, and machine learning researchers."
    ),

    html.Hr(),

    html.H2("Patient Information"),

    html.Label("Age"),
    dcc.Slider(
        id="age",
        min=20,
        max=100,
        step=1,
        value=50,
        marks={20: "20", 40: "40", 60: "60", 80: "80", 100: "100"}
    ),

    html.Br(),

    html.Label("Sex"),
    dcc.Dropdown(
        id="sex",
        options=[
            {"label": "Female", "value": 1},
            {"label": "Male", "value": 2}
        ],
        value=1
    ),

    html.Label("Systolic Blood Pressure"),
    dcc.Input(
        id="systolic_bp",
        type="number",
        value=120
    ),

    html.Label("Diastolic Blood Pressure"),
    dcc.Input(
        id="diastolic_bp",
        type="number",
        value=80
    ),

    html.Label("Cholesterol"),
    dcc.Dropdown(
        id="cholesterol",
        options=[
            {"label": "Normal", "value": 1},
            {"label": "Above normal", "value": 2},
            {"label": "Well above normal", "value": 3}
        ],
        value=1
    ),

    html.Label("Glucose"),
    dcc.Dropdown(
        id="glucose",
        options=[
            {"label": "Normal", "value": 1},
            {"label": "Above normal", "value": 2},
            {"label": "Well above normal", "value": 3}
        ],
        value=1
    ),

    html.Label("Smoking Status"),
    dcc.Dropdown(
        id="smoking",
        options=[
            {"label": "No", "value": 0},
            {"label": "Yes", "value": 1}
        ],
        value=0
    ),

    html.Label("Alcohol Intake"),
    dcc.Dropdown(
        id="alcohol",
        options=[
            {"label": "No", "value": 0},
            {"label": "Yes", "value": 1}
        ],
        value=0
    ),

    html.Label("Physical Activity"),
    dcc.Dropdown(
        id="activity",
        options=[
            {"label": "No", "value": 0},
            {"label": "Yes", "value": 1}
        ],
        value=1
    ),

    html.Label("BMI"),
    dcc.Slider(
        id="bmi",
        min=15,
        max=50,
        step=0.1,
        value=25,
        marks={15: "15", 25: "25", 35: "35", 50: "50"}
    ),

    html.Hr(),

    html.H2("Prediction Result"),
    html.Div(id="prediction_output"),

    html.Hr(),

    dcc.Tabs([

        dcc.Tab(label="Patient Explanation", children=[
            html.Br(),
            html.Div(id="patient_explanation")
        ]),

        dcc.Tab(label="Clinician Explanation", children=[
            html.Br(),
            html.Div(id="clinician_explanation"),
            dcc.Graph(id="clinician_feature_chart")
        ]),

        dcc.Tab(label="ML Researcher View", children=[
            html.Br(),
            html.Div(id="researcher_explanation"),
            dcc.Graph(id="researcher_feature_chart")
        ]),

        dcc.Tab(label="Ethics and Safety", children=[
            html.Br(),
            html.H3("Important Notice"),
            html.P(
                "This dashboard is for educational and research demonstration only. "
                "It is not a medical diagnostic tool."
            ),
            html.P(
                "Predictions may be affected by dataset bias, missing clinical variables, "
                "and limitations of the trained machine learning model."
            ),
            html.P(
                "Clinical decisions should always involve qualified healthcare professionals."
            )
        ])
    ])
])


# Create helper function for prediction

def create_patient_dataframe(
    age,
    sex,
    systolic_bp,
    diastolic_bp,
    cholesterol,
    glucose,
    smoking,
    alcohol,
    activity,
    bmi
):
    patient_df = pd.DataFrame([{
        "Age": age,
        "Sex": sex,
        "Systolic_BP": systolic_bp,
        "Diastolic_BP": diastolic_bp,
        "Cholesterol": cholesterol,
        "Glucose": glucose,
        "Smoking_status": smoking,
        "Alcohol_intake": alcohol,
        "Physical_activity": activity,
        "BMI": bmi
    }])

    return patient_df[features]


# Create feature contribution approximation

def get_feature_importance_table(patient_df):
    """
    This uses model feature importance as a simple fallback explanation.
    Later, you can replace this with SHAP values.
    """

    importance_df = pd.DataFrame({
        "Feature": features,
        "Patient Value": patient_df.iloc[0].values,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    return importance_df


# Dashboard callback

@app.callback(
    Output("prediction_output", "children"),
    Output("patient_explanation", "children"),
    Output("clinician_explanation", "children"),
    Output("researcher_explanation", "children"),
    Output("clinician_feature_chart", "figure"),
    Output("researcher_feature_chart", "figure"),

    Input("age", "value"),
    Input("sex", "value"),
    Input("systolic_bp", "value"),
    Input("diastolic_bp", "value"),
    Input("cholesterol", "value"),
    Input("glucose", "value"),
    Input("smoking", "value"),
    Input("alcohol", "value"),
    Input("activity", "value"),
    Input("bmi", "value")
)
def update_dashboard(
    age,
    sex,
    systolic_bp,
    diastolic_bp,
    cholesterol,
    glucose,
    smoking,
    alcohol,
    activity,
    bmi
):

    patient_df = create_patient_dataframe(
        age,
        sex,
        systolic_bp,
        diastolic_bp,
        cholesterol,
        glucose,
        smoking,
        alcohol,
        activity,
        bmi
    )

    prediction = model.predict(patient_df)[0]
    probability = model.predict_proba(patient_df)[0][1]

    if probability < 0.40:
        risk_level = "Low"
    elif probability < 0.70:
        risk_level = "Medium"
    else:
        risk_level = "High"

    importance_df = get_feature_importance_table(patient_df)

    top_features = importance_df.head(3)

    prediction_output = html.Div([
        html.H3(f"Estimated Risk Level: {risk_level}"),
        html.H4(f"Predicted Probability: {probability:.1%}"),
        html.P(
            "Prediction class: Cardiovascular disease"
            if prediction == 1
            else "Prediction class: No cardiovascular disease"
        )
    ])

    patient_explanation = html.Div([
        html.H3("Patient-Friendly Explanation"),
        html.P(
            f"The model estimates your cardiovascular risk as {risk_level.lower()}."
        ),
        html.P(
            "The main factors considered important for this prediction were:"
        ),
        html.Ul([
            html.Li(f"{row['Feature']}") for _, row in top_features.iterrows()
        ]),
        html.P(
            "This result is for educational purposes only and should not be used as a medical diagnosis."
        )
    ])

    clinician_explanation = html.Div([
        html.H3("Clinician Explanation"),
        html.P(f"Predicted probability of cardiovascular disease: {probability:.4f}"),
        html.P(f"Predicted class: {prediction}"),
        html.P(
            "The chart below shows the most influential features according to the trained Gradient Boosting model."
        )
    ])

    researcher_explanation = html.Div([
        html.H3("Machine Learning Researcher View"),
        html.P("Model used: Gradient Boosting Classifier"),
        html.P(
            "Feature importance values are extracted from the fitted Gradient Boosting model."
        ),
        html.P(
            "For deeper explainability, this section can be extended with SHAP summary plots, "
            "waterfall plots, and local feature contribution values."
        )
    ])

    clinician_fig = px.bar(
        importance_df.head(10),
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top Model Feature Importances"
    )

    clinician_fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    researcher_fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Global Feature Importance for Gradient Boosting"
    )

    researcher_fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    return (
        prediction_output,
        patient_explanation,
        clinician_explanation,
        researcher_explanation,
        clinician_fig,
        researcher_fig
    )


# Run the app

if __name__ == "__main__":
    app.run(debug=True)