# 🔍 AI-Powered User Churn Predictor

A machine learning project that predicts which users are likely to stop using a SaaS product, based on behavior and usage data.

---

## 🚀 Features
- 📂 Upload CSV files of user activity (e.g., from your SaaS platform)
- 🔍 Predict user churn using a pre-trained Random Forest model
- 📊 Visualize key factors that influence churn
- 🖥️ Simple Flask-based web interface for predictions

---

## 🧠 Tech Stack
- **Backend:** Python, Flask
- **ML & Data:** Scikit-learn, Pandas, Matplotlib, Joblib
- **Frontend:** HTML (Jinja2 Templates)

---

## 📁 Project Structure
```
churn-predictor/
├── app/
│   ├── app.py                # Flask web server
│   ├── templates/index.html  # Frontend UI
│   └── model/churn_model.pkl # Trained model (generated after training)
├── archive/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Sample dataset
├── notebooks/
│   └── churn_analysis.ipynb  # EDA + model training walkthrough
├── train_model.py            # Script to train and save the model
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model
```bash
python train_model.py
```
This will save the trained model to `app/model/churn_model.pkl`.

> 🔧 **Note:** If `churn_model.pkl` is not included in this repo, you must generate it by running `train_model.py`.

### 3️⃣ Start the Flask App
```bash
cd app
python app.py
```
Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## 📊 Dataset

We use the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) which contains customer usage behavior and contract details.

---

## 📌 Future Improvements
- Add SHAP or LIME interpretability for feature importance
- Integrate model retraining pipeline
- Dockerize the full app

---

## 👨‍💻 Author
**Md Arafat** — [GitHub Profile](https://github.com/mdarafatrealworld01)

---

## 📄 License
MIT License — *Free to use with attribution*
