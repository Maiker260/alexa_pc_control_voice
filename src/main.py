import json
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

with open("app_config.json") as f:
    config = json.load(f)

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

    print(f"Intent recibido: {intent}")

    return {"status": "ok"}