from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .routers import tasks, sensors

app = FastAPI(title="Mini REST API", version="1.0.0")

# CORS (optional anpassen)
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Router
app.include_router(tasks.router)
app.include_router(sensors.router)

@app.on_event("startup")
def on_startup():
init_db()

@app.get("/")
def root():
return {"status": "ok", "docs": "/docs"}