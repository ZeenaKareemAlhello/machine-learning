import pickle

C = 1.0
file_name = f"model_C={C}.bin"

customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85,
}

with open(file_name, "rb") as f_in:
    dv, model = pickle.load(f_in)


X = dv.transform([customer])
X

model.predict_proba(X)

y_pred = model.predict_proba(X)[0, 1]

print("input", customer)
print(f"churn probability", y_pred)
