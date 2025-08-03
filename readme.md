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

## 🚀 How It Works

1. `embed.py`: Embeds the story using OpenAI (or HuggingFace) embeddings and saves them to `chroma.db`.
2. `chunk.py`: Loads the DB, accepts user questions, and retrieves relevant chunks.
3. A prompt is generated combining the **question + context** and sent to a language model (e.g., GPT-3.5/4) to generate an answer.

## 🧪 Example Question

```python
question = "What magic did Linghu Chong comprehend?"
```
Output:

Linghu Chong comprehended a magic that was a burst of flame, which he humorously dubbed the "Bursting Break." This magic was a fusion of Dugu Nine Sword philosophy with slime physiology...

## 📚 Story Background
The data.md file contains a translated wuxia-meets-isekai narrative where:

Linghu Chong dies heroically, is reincarnated as a slime, and develops mana-based martial arts

He invents powerful flame techniques by combining (Dugu Nine Swords) with magic physiology

Eventually becomes known as the Flameburst Sword Sage Slime

## 🛠 Requirements
Python 3.8+

ChromaDB

OpenAI API

dotenv, tqdm, langchain, chromadb


