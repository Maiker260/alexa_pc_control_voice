from fastapi import FastAPI, Request, HTTPException
from src.utils.get_api_key import get_api_key

app = FastAPI()

@app.get("/health-626089")
def health():
    return {"status": "ok"}

@app.post("/alexa")
async def alexa(request: Request):
    print(request.headers)
    if not request.headers.get("cf-ray"):
        raise HTTPException(status_code=403, detail="Forbidden")
    
    API_KEY = get_api_key()
    print(request.headers.get("x-api-key"))

    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    intent = (
        data.get("intent") or
        data.get("request", {}).get("intent", {}).get("name")
    )

    if not intent:
        raise HTTPException(status_code=400, detail="Invalid request")

    print(f"Intent received: {intent}")

    return {"status": "ok"}