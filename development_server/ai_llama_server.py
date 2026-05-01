from fastapi import FastAPI
import requests

app = FastAPI()

LLAMA_URL = "http://127.0.0.1:8080/completion"


@app.get("/generate")
def generate(prompt: str):
    response = requests.post(
        LLAMA_URL,
        json={
            "prompt": prompt,
            "n_predict": 50
        }
    )

    return response.json()
