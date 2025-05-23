# 🧠 Mangakensaku

Mangakensaku is a simple yet powerful FastAPI-based application that takes a text query and retrieves the most relevant manga panels. It was built primarily to understand how FAISS works for similarity search over image embeddings.


![Demo](app/static/angry.gif)
![Demo](app/static/hi.gif)
![Demo](app/static/explosion.gif)
## 🚀 Features

- 🔍 Search manga panels using natural language queries
- 🖼️ Retrieve semantically similar images using CLIP embeddings
- ⚡ Fast approximate nearest neighbor search powered by FAISS
- ✅ Normalized embeddings + `IndexFlatIP` for best performance

## 🛠️ Tech Stack

- **FastAPI** for API framework
- **FAISS** for efficient similarity search
- **CLIP** for text & image embeddings
- **Python** for the backend logic

## 🧪 How It Works

1. A query is embedded using the CLIP model.
2. The embedding is **normalized** to unit length.
3. FAISS retrieves top-k most relevant images using `IndexFlatIP`.
4. Relevant manga panel URLs or paths are returned.

> Note: FAISS `IndexFlatIP` works best with normalized embeddings because it uses inner product (which becomes cosine similarity when vectors are normalized).

## 🧰 Setup

```bash
git clone https://github.com/yourusername/mangakensaku.git
cd mangakensaku
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

#### Image Credit
`https://panelsdesu.com/`