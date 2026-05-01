GNU nano 9.0          aiserver.py
from fastapi import FastAPI
import subprocess

app = FastAPI()

MODEL_PATH = "tinyllama-1.1b-chat-v1.0-q4_k_m.gguf"


@app.get("/")
def home():
    return {"message": "AI server running 🚀"}


@app.get("/generate")
def generate(prompt: str):
    try:
        result = subprocess.run(
            [
                "llama-cli",
                "-m", MODEL_PATH,
                "-n", "50",          # 👈 reduce tokens
                "-t", "4",
                "--temp", "0.7"
            ],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=20   # 👈 HARD STOP after 20 sec
        )

        output = result.stdout + result.stderr

        return {"response": output}

    except subprocess.TimeoutExpired:
        return {"error": "Model took too long (stopped)>

    except Exception as e:
        return {"error": str(e)}
