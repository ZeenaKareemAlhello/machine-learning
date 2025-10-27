import pickle

file_name = "pipeline_v1.bin"

with open(file_name, "rb") as f_in:
    pipeline = pickle.load(f_in)

rec = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
}
result = pipeline.predict_proba(rec)[0, 1]
print(result)
