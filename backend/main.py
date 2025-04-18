from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI(
    title="Link Shortener Backend",
    description="A simple link shortener backend using FastAPI.",
    version="0.2",
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
