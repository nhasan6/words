from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.db.connection import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.models.word import Word

router = APIRouter(prefix="/graph")

@router.get("/")
async def get_graph(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Word).options(selectinload(Word.source)))
    words = result.scalars().all()
    nodes = [{"id": w.id, "text": w.text, "type": w.type} for w in words]
    links = []

    for i in range(len(words)):
        for j in range (i + 1, len(words)):
            score = 0
            if words[i].type is not None and words[j].type is not None and words[i].type == words[j].type:
                score += 0.5
            if words[i].source_id is not None and words[j].source_id is not None:
                if words[i].source_id == words[j].source_id:
                    score += 3
                elif words[i].source.title.lower() == words[j].source.title.lower():
                    score += 3
            if words[i].speaker is not None and words[j].speaker is not None:
                s1 = words[i].speaker.lower()
                s2 = words[j].speaker.lower() 
                if s1 in s2 or s2 in s1:
                    score += 2
            if words[i].tags and words[j].tags:
                score += len(set(words[i].tags) & set(words[j].tags))
            if score > 0:
                links.append({"source": words[i].id, "target": words[j].id, "strength": score})
    
    # normalize data 
    if links:
        max_strength = max(link['strength'] for link in links)
        min_strength = min(link['strength'] for link in links)
        spread = max_strength - min_strength

        for link in links:
            link['strength'] = (link['strength'] - min_strength) / spread if spread > 0 else 1.0

    return {"nodes": nodes, "links": links}