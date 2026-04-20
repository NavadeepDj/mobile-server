from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your phone API is running 🚀"}

@app.get("/generate")
def generate(prompt: str):
    return {"response": f"You said: {prompt}"}
