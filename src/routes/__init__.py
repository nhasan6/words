from fastapi import FastAPI
from src.routes.auth import router as auth_router
from src.routes.words import router as word_router
from src.routes.sources import router as source_router


def include_routers(app: FastAPI): 
    app.include_router(auth_router)
    app.include_router(word_router)
    app.include_router(source_router)

