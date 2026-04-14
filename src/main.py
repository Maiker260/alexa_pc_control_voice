from fastapi import FastAPI, Request, HTTPException
from src.utils.get_api_key import get_api_key
from src.handlers.handle_request import handle_request

app = FastAPI()

@app.get("/health-626089")
def health():
    return {"status": "ok"}

@app.post("/alexa")
async def alexa(request: Request):
    if not request.headers.get("cf-ray"):
        raise HTTPException(status_code=403, detail="Forbidden")
    
    API_KEY = get_api_key()
    # NEED TO DELETE THE PRINT
    print(request.headers.get("x-api-key"))

    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    try:
        result = handle_request(data)

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }