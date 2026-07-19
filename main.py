from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.db.connection import init_db
from contextlib import asynccontextmanager
from src.routes import include_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # everything b4 yield runs when the server starts up
    print("server is starting .....")
    await init_db()
    yield

    # everything after yield runs when the server shuts down
    print ("server is stopping ....")

app = FastAPI(lifespan=lifespan)
include_routers(app)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}