from typing import Literal
from fastapi import FastAPI
import pickle
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="homework")
file_name = "pipeline_v2.bin"

with open(file_name, "rb") as f_in:
    pipeline = pickle.load(f_in)


class Client(BaseModel):
    lead_source: Literal["organic_search"]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)


@app.post("/predict")
def predict(client: Client):

    print(client)
    client = Client.model_validate(client)
    y_pred = pipeline.predict_proba(client.model_dump())[0, 1]

    result = {"score": float(y_pred)}

    return result


# if __name__ == "__main__":
#     uvicorn.run("service:app", host="0.0.0.0", port=9696, reload=True)
