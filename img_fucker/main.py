import uvicorn
from logger import log
from api.v1.api import app
from config import settings

if __name__ == "__main__":
    log.info("Starting the API server...")
    uvicorn.run(app, host=settings.api_host, port=settings.api_host_port)