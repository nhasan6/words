from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import numpy as np

from src.db.connection import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.word import Word
from src.db.models.word_embedding import WordEmbedding


router = APIRouter(prefix="/graph")

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a)) * np.linalg.norm(b))

@router.get("/")
async def get_graph(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Word).options(selectinload(Word.source)))
    words = result.scalars().all()

    embeddings_result = await db.execute(select(WordEmbedding))
    embeddings_by_word = {e.word_id: e.embedding for e in embeddings_result.scalars().all()}

    nodes = [{"id": w.id, "text": w.text, "type": w.type, "definition": w.definition} for w in words]
    links = []

    for i in range(len(words)):
        for j in range (i + 1, len(words)):
            metadata_score = 0
            if words[i].type is not None and words[j].type is not None and words[i].type == words[j].type:
                metadata_score += 0.5
            if words[i].source_id is not None and words[j].source_id is not None:
                if words[i].source_id == words[j].source_id:
                    metadata_score += 3
                elif words[i].source.title.lower() == words[j].source.title.lower():
                    metadata_score += 3
            if words[i].speaker is not None and words[j].speaker is not None:
                s1 = words[i].speaker.lower()
                s2 = words[j].speaker.lower() 
                if s1 in s2 or s2 in s1:
                    metadata_score += 2
            if words[i].tags and words[j].tags:
                metadata_score += len(set(words[i].tags) & set(words[j].tags))

            emb_i = embeddings_by_word.get(words[i].id)
            emb_j = embeddings_by_word.get(words[j].id)
            semantic_score = cosine_similarity(emb_i, emb_j) if emb_i and emb_j else 0

            if metadata_score > 0 or semantic_score > 0:
                links.append({
                    "source": words[i].id, 
                    "target": words[j].id, 
                    "metadata_score": metadata_score,
                    "semantic_score": semantic_score
                })
    
    # normalize data 
    if links:
        meta_vals = [l["metadata_score"] for l in links]
        sem_vals = [l["semantic_score"] for l in links]

        meta_min, meta_max = min(meta_vals), max(meta_vals)
        sem_min, sem_max = min(sem_vals), max(sem_vals)
        meta_spread = meta_max - meta_min
        sem_spread = sem_max - sem_min

        metadata_weight = 0.4
        semantic_weight = 0.6

        for link in links:
            norm_meta = (link["metadata_score"] - meta_min) / meta_spread if meta_spread > 0 else 1.0
            norm_sem = (link["semantic_score"] - sem_min) / sem_spread if sem_spread > 0 else 1.0
            link["strength"] = metadata_weight * norm_meta + semantic_weight * norm_sem
            del link["metadata_score"]
            del link["semantic_score"]

    return {"nodes": nodes, "links": links}