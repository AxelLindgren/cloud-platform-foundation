from fastapi import FastAPI, Request
import os
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

VERSION = os.getenv("APP_VERSION", "dev")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"{request.method} {request.url.path}")
    response = await call_next(request)
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": VERSION}
