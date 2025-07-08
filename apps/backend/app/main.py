from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import Settings
from .router import chat, items, root

settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3900"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(items.router)
app.include_router(chat.router)


@app.get("/info")
async def info():
    return {
        "name": "backend",
        "version": "0.1.0",
        "host": settings.host,
        "port": settings.port,
        "reload": settings.reload,
        "lifespan": settings.lifespan,
    }
