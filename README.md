# 🎬 CineMatch AI — Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-F7931E?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An end-to-end Machine Learning web application built from scratch that generates movie recommendations using Content-Based Filtering. The core engine vectorizes movie metadata using **TF-IDF** and computes spatial proximity using **Cosine Similarity**.

---

## 📌 Features

- **Fault-Tolerant Lookup:** Handles lowercased queries, whitespace variations, and spelling typos using `difflib`.
- **TF-IDF Feature Extraction:** Converts categorical genre tags into informative numerical embeddings.
- **Cosine Similarity Engine:** Calculates pairwise distance across feature vectors in real time.
- **Pre-computed Artifacts:** Model serialization via `pickle` guarantees sub-millisecond query responses.
- **Interactive UI:** Web dashboard built with Streamlit featuring dynamic sliders and match percentage metrics.

---

## 🛠️ Tech Stack & Concepts

- **Frontend / Web:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Machine Learning & NLP:** Scikit-Learn (`TfidfVectorizer`, `cosine_similarity`)
- **String Matching:** `difflib` (Gestalt Pattern Matching)
- **Model Serialization:** Pickle

---

## 📁 Repository Structure

```text
├── app.py              # Streamlit application UI and recommendation engine
├── movies.pkl          # Serialized preprocessed DataFrame
├── similarity.pkl      # Pre-computed pairwise Cosine Similarity matrix
├── tfidf.pkl           # Trained TF-IDF Vectorizer instance
├── requirements.txt    # Python runtime dependencies
└── README.md           # Documentation