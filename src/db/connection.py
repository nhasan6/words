from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.config import Settings
from sqlalchemy import text
from src.db.models import Base, User

settings = Settings()

# build connection string from .env variables
# @db refers to Docker container name 
DB_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@db/{settings.POSTGRES_DB}"

# creates the connection to Postgres using asyncpg
# echo = True --> makes SQLAlchemy print every SQL cmd it runs to the console
engine = create_async_engine(url=DB_URL, echo=True)

# create factory to produce db sessions
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database initialized and tables created if they did not exist")
        
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session # fastapi opens the session b4 our route runs and automatically closes the session after