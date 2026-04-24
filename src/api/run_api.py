import uvicorn

def run_api(app):
    print("Starting FastAPI...")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
    print("Running...")