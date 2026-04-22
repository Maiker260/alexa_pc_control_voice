from fastapi import FastAPI, Request, Response, HTTPException
from src.utils.get_keys import get_keys
from src.handlers.handle_request import handle_request

app = FastAPI()

@app.middleware("http")
async def block_unwanted(request: Request, call_next):
    if request.url.path != "/alexapc" or request.method != "POST":
        return Response(status_code=404)
    
    return await call_next(request)

@app.post("/alexapc")
async def alexa(request: Request):    
    API_KEY, DEVICE_SECRET = get_keys()

    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401)
    
    if request.headers.get("x-device-secret") != DEVICE_SECRET:
        raise HTTPException(status_code=403)
    
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