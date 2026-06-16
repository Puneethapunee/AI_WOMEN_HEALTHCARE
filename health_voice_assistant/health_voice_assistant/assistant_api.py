from fastapi import FastAPI
from main_controller import process_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Assistant API running"}

@app.get("/ask")
def ask(query: str):
    response = process_query(query)
    return {"response": response}