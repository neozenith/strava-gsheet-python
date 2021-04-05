# Strava Google Sheet - Python

Connecting my Strava activities to my Google Sheets workout tracking using Python.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

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

## Getting logs

```
heroku logs -a APP_NAME --tail
```
