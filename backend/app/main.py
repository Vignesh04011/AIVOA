from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine
from app.database.models import Base
from app.api.routes import router
from app.api.ai_routes import router as ai_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HCP CRM API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers AFTER creating app
app.include_router(router)
app.include_router(ai_router)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "HCP CRM Backend Running 🚀"
    }