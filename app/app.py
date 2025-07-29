from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = joblib.load(os.path.join("app", "model", "churn_model.pkl"))  #

categorical_cols = [
    'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
    'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
    'PaperlessBilling', 'PaymentMethod'
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_csv(file)

        if 'customerID' in df.columns:
            df = df.drop(columns=["customerID"])

        for col in categorical_cols:
            if col in df.columns:
                df[col] = LabelEncoder().fit_transform(df[col])

        df = df.fillna(0)

        predictions = model.predict(df)
        return render_template("index.html", results=predictions.tolist())
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
