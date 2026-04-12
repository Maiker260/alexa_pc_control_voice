import uvicorn

def run_api(app):
    print("Starting FastAPI...")
    uvicorn.run(app, host="0.0.0.0", port=8000)