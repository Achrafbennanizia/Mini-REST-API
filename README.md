# Timeout Backend

A robust, production-ready Node.js backend API built with Express, MongoDB, JWT-based authentication, and rate-limiting middleware.  
Ideal for handling user sessions, timeouts and secure API access.

## 🔍 Features

- User authentication & authorization (JWT)
- Rate limiting to protect endpoints from abuse
- MongoDB data models (via Mongoose)
- Clear project structure: controllers, models, routes, middleware
- Environment-based configuration for secure deployment
- Ready for both development (with hot-reload) and production usage

## 🛠️ Tech Stack

- **Runtime / Framework**: Node.js + Express
- **Database**: MongoDB (via Mongoose)
- **Auth**: JSON Web Tokens (JWT)
- **Rate Limiting**: Express rate-limit or custom middleware
- **Env Config**: dotenv
- **Structure**: MVC-style separation (controllers, models, routes, middleware)
- **Others**: bcrypt for password hashing, cookie-parser, CORS support, etc.

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Achrafbennanizia/backend.git
cd backend
```

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/xb5628kgrk-commits/Mini-REST-API.git
cd Mini-REST-API

---
### 2. Create a virtual environment

macOS / Linux:
python -m venv .venv
source .venv/bin/activate
Windows:
python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Start the development server
uvicorn app.main:app --reload
API runs at:
👉 http://127.0.0.1:8000
Swagger UI:
👉 http://127.0.0.1:8000/docs
```
