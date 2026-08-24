from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Digital Twin Running"
    }