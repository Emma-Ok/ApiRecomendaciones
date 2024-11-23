from fastapi import FastAPI

app = FastAPI()

from .main import router
app.include_router(router)