from flask import Flask, jsonify, request
import pickle

app = Flask("churn")

C = 1.0
file_name = f"model_C={C}.bin"

with open(file_name, "rb") as f_in:
    dv, model = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    print(customer)
    X = dv.transform([customer])
    model.predict_proba(X)
    y_pred = model.predict_proba(X)[0, 1]

    churn = y_pred >= 0.5
    result = {"churn_probability": float(y_pred), "churn": bool(churn)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
