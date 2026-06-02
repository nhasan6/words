from fastapi import FastAPI
from src.db.connection import init_db
from contextlib import asynccontextmanager
from src.routes.auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # everything b4 yield runs when the server starts up
    print("server is starting .....")
    await init_db()
    yield

    # everything after yield runs when the server shuts down
    print ("server is stopping ....")

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}