# Strava Google Sheet - Python

Connecting my Strava activities to my Google Sheets workout tracking using Python.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Setup Dev Environment

```bash
# Using OAPIv3 codegen
brew install swagger-codegen
swagger-codegen generate -i https://developers.strava.com/swagger/swagger.json -l python -o strava

# Setup python development
python3 -m venv .venv
. .venv/bin/activate
./tasks.py install
```

## Testing

```
./tasks.py test
```

## Running the server

```
./tasks.py dev
```

## Getting logs

```
./tasks.py logs --tail
```
