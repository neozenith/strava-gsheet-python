# Strava Google Sheet - Python

Connecting my Strava activities to my Google Sheets workout tracking using Python.

## Setup Dev Environment

```
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt --upgrade
```

## Testing

```
python -m pytest
```

## Running the server

```
uvicorn api.v1:app
```
