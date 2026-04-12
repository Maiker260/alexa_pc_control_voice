from fastapi import FastAPI, Request, HTTPException
from src.utils.get_api_key import get_api_key

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/alexa")
async def alexa(request: Request):
    API_KEY = get_api_key()

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