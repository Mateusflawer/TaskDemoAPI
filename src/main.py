from fastapi import FastAPI
import uvicorn
from .api.routers import api_router

app = FastAPI(title="TaskDemoAPI", version="0.1.1")

# Inclui os roteadores da API
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
