from fastapi import FastAPI

app = FastAPI(title="Student Database API")

@app.get("/")
def home():
    return {"message": "Welcome to the Student Database API!"}
