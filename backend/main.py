from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"Link": "Shortener"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)