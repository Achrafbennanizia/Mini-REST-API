# Mini-REST-API (FastAPI)

**Ziel:** CRUD für _Tasks_ & _Sensorwerte_. Schnelle Demo für Software‑Engineering/Backend (2–3h).

## Features

- **CRUD**: GET, POST, PUT, DELETE
- **Modelle**: SQLModel + Pydantic
- **DB**: SQLite (Datei `app.db`)
- **API‑Doku**: `/docs` & `/redoc`
- **Tests**: pytest
- **Docker** & **Makefile**

## Schnellstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
# Mini-REST-API
