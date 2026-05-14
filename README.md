<div align="center">

# 🔗 My First API

### Cloud-Deployed REST API with FastAPI & MongoDB

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://mongodb.com)
[![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app)

**A production-ready REST API built with FastAPI and MongoDB Atlas, deployed live on Railway cloud. Manages skills and personal data with full CRUD operations and interactive Swagger documentation.**

[🌐 Live API](https://my-first-api-production-42c4.up.railway.app/my-info) · [📖 Swagger Docs](https://my-first-api-production-42c4.up.railway.app/docs)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🚀 **Live Deployment** | Fully deployed and accessible on the internet via Railway |
| 📊 **MongoDB Integration** | Connected to cloud-hosted MongoDB Atlas for persistent storage |
| 📖 **Auto-Generated Docs** | Interactive Swagger UI documentation at `/docs` |
| 🔄 **CRUD Operations** | Create, Read skills and personal info via REST endpoints |
| ⚡ **High Performance** | Built on FastAPI — one of the fastest Python web frameworks |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Database** | MongoDB Atlas (Cloud) |
| **Deployment** | Railway Cloud |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/my-info` | Returns personal info and skills |
| `POST` | `/add-skill` | Add a new skill to the database |
| `GET` | `/get-skill` | Retrieve stored skills |
| `GET` | `/docs` | Interactive Swagger API documentation |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/ravi-ai-dev/my-first-api.git
cd my-first-api

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload
```

Open **http://localhost:8000/docs** for Swagger UI.

---

## 📁 Project Structure

```
my-first-api/
├── main.py              # FastAPI application with all routes
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 📄 License

Open source — feel free to fork and build upon it.

---

<div align="center">

**Built with ❤️ by [Ravi Singh](https://github.com/ravi-ai-dev)**

</div>
