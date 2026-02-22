from fastapi import FastAPI
from app.fetch import fetch_users
from app.transform import transform_users
from app.writer import write_to_parquet

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Service is running"}

@app.get("/run")
def run_pipeline():
    users = fetch_users()
    transformed = transform_users(users)
    write_to_parquet(transformed)
    return {"message": "Pipeline executed successfully"}