# Connections 🔗

## Background

When I read books on my iPhone and stumble across unfamiliar words, the ambitious logophile in me takes a screenshot of the word + definition, determined to "save it" for future use. Unfortunately, all that happens is that my phone runs out of storage capacity  and I never look at the screenshots again. 

I designed "Connections" in hopes of addressing this issue and freeing up my phone storage. Connections visualizes each word as a 3D node on a fully interactive graph, and uses ML to highlight the semantic links between different terms. I've also kept metadata-based links, so I can trace back to the book, show, or podcast where I first discovered each word. 

## Tech Stack

- **Backend:** FastAPI 
- **Database:** PostgreSQL 
- **Embeddings:** [sentence-transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (`all-MiniLM-L6-v2`)
- **Vector storage:** pgvector (Postgres extension)
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Auth:** JWT (pyjwt) + pwdlib (argon2 hashing)
- **Frontend:** Vanilla JS + [3d-force-graph](https://github.com/vasturiano/3d-force-graph) (ThreeJS/WebGL), served as static files via FastAPI
- **Containerization:** Docker

## Features
- **Metadata-based connections** - links between words based on shared source, speaker, type, and tags 
- **Semantic connections & automatic embeddings** - an embedding model conputes conceptual similarity between words, so terms with related meanings connect even without shared metadata
- **Combined link strength** - each connection blends both scores, normalized independently before combining
- **Interactive 3D graph** - full rotate, zoom, and pan functionality. Clicking on any word opens a detailed panel complete with the definition, speaker, quote, etc. 

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
