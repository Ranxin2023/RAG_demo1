# 🔥 RAG-Powered QA System Featuring "Rebirth of Linghu Chong"

This project implements a simple yet powerful **Retrieval-Augmented Generation (RAG)** system using Python, focused on answering questions about a fantasy-themed narrative where **Linghu Chong**, a martial arts master, is reincarnated as a slime in a magical world.

## 🧠 Project Overview

The RAG pipeline allows users to query a rich `.md` file (`data.md`) containing the translated story **"Rebirth of Linghu Chong"**, and receive accurate, context-aware answers in English.

> Example:
> - ❓ *What magic did Linghu Chong comprehend?*
> - ✅ *Linghu Chong comprehended a magic that was a burst of flame, humorously dubbed "Bursting Break"...*

## 🗂 File Structure

```graphql
AGENT2_RAG/
│
├── chunk.py # Splits the story into context chunks
├── embed.py # Generates embeddings and stores them in vector DB
├── data.md # English-translated story data (Linghu Chong's reincarnation as a slime)
├── chroma.db # Persisted vector database (Chroma)
├── .env # Environment variables (e.g., OpenAI keys)
├── .gitignore
├── readme.md # Project README (you are here)
└── pycache/ # Python cache
```

