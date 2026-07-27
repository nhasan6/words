# Words

description to be added

## Tech Stack

 **Backend:** FastAPI 
- **Database:** PostgreSQL 
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Auth:** JWT (pyjwt) + pwdlib (argon2 hashing)
- **Frontend:** Vanilla JS + [3d-force-graph](https://github.com/vasturiano/3d-force-graph) (ThreeJS/WebGL), served as static files via FastAPI
- **Containerization:** Docker

## Setup

1. Clone the repo.
2. Create a `.env` file in the project root:
```
   POSTGRES_USER=...
   POSTGRES_PASSWORD=...
   POSTGRES_DB=words
   SECRET_JWT_KEY=...   # generate with: openssl rand -hex 32
```
3. Start the containers:
```
   docker compose up
```
4. Create the owner account (only needs to be run once, or again after `docker compose down -v`):
```
   docker compose exec app python temp_script.py
```
5. Open the app at `http://localhost:8000/static/`.