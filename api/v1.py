"""Main API entrypoint."""

# Third Party Libraries
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root handler."""
    return {"message": "Hello World"}
