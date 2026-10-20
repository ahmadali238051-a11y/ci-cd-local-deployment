from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD pipeline project is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}