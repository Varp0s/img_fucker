from fastapi import FastAPI
from .endpoints import analyze_img
import uvicorn

app = FastAPI()

app.include_router(analyze_img.router)

@app.get("/")
async def read_root():
    return {"message": "Server is running! To use, visit /analyze_img/ and upload your image"}

