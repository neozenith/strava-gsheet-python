"""Main API entrypoint."""

# Standard Library
from pprint import pprint as pp

# Third Party Libraries
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()


app = FastAPI()


@app.get("/")
async def status():
    """Root handler."""
    return {"message": "Hello World"}


@app.post("/")
async def webhook(event: Request):
    """Webhook accepting any JSON payload and just returning it."""
    jsonData = await event.json()
    pp(jsonData)
    return jsonData
