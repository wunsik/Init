from fastapi import FastAPI
from .routes.inventory import router as inventory_router

app = FastAPI(title="AI Harness API", version="0.1.0")
app.include_router(inventory_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
