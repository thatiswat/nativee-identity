from fastapi import FastAPI

app = FastAPI(
    title="Nativeee Identity",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "identity",
        "status": "running",
    }