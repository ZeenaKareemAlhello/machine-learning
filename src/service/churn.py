from fastapi import FastAPI
import pickle
from typing import Dict, Any
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="churn")

C = 1.0
file_name = f"model_C={C}.bin"

with open(file_name, "rb") as f_in:
    dv, model = pickle.load(f_in)


# request
class Customer(BaseModel):
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0)
    totalcharges: float = Field(..., ge=0.0)


class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool


@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:

    print(customer)
    customer = Customer.model_validate(customer)
    X = dv.transform([customer.model_dump()])
    model.predict_proba(X)
    y_pred = model.predict_proba(X)[0, 1]

    churn = y_pred >= 0.5
    result = {"churn_probability": float(y_pred), "churn": bool(churn)}

    return PredictResponse.model_validate(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
