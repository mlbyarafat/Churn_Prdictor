import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"archive\\WA_Fn-UseC_-Telco-Customer-Churn.csv") # Kindly here you have to use your path to load dataset. 

# Basic preprocessing
df = df.dropna()
df = df.drop(columns=["customerID"])

# Encode categorical columns
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "app/model/churn_model.pkl")

print("Model trained and saved to app/model/churn_model.pkl")
