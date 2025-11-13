# Mini-REST-API (FastAPI)

A lightweight, production-ready REST API built with FastAPI.
This project demonstrates clean API design, modular structure, Docker support, and simple database integration.
Perfect for learning, practicing backend development, or extending into real microservices.

---

## 🚀 Tech Stack

- **Python** (FastAPI)
- **Uvicorn** ASGI server
- **SQLModel / Pydantic** for models & validation
- **SQLite** as embedded database (`app.db`)
- **Pytest** for testing
- **Docker** + **Makefile** for easy run & build

---

## 📦 Project Structure

```text
Mini-REST-API/
├─ app/
│  ├─ main.py          # FastAPI application entrypoint
│  ├─ ...              # models, routers, db logic (see code)
├─ tests/              # pytest tests
├─ Dockerfile          # container image
├─ Makefile            # helper commands
├─ requirements.txt    # Python dependencies
└─ README.md
