from sentence_transformers import SentenceTransformer

_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model: SentenceTransformer | None = None


def load_embedding_model() -> None:
    global embedding_model
    embedding_model = SentenceTransformer(_MODEL_NAME)


def encode_word(text: str, definition: str | None) -> list[float]:
    if embedding_model is None:
        raise RuntimeError("Embedding model not loaded — call load_embedding_model() at startup")
    combined = f"{text}. {definition or ''}"
    return embedding_model.encode(combined).tolist()