import json
from fastapi import FastAPI, Request, HTTPException
from api.load_config import load_config

app = FastAPI()

config = load_config()

API_KEY = config["api_key"]

@app.post("/alexa")
async def alexa(request: Request):
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    data = await request.json()

    intent = (
        data.get("intent") or
        data.get("request", {}).get("intent", {}).get("name")
    )

    if not intent:
        raise HTTPException(status_code=400, detail="Invalid request")

    print(f"Intent received: {intent}")

    return {"status": "ok"}