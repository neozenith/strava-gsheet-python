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

## Getting Google Service Account Credentials

[gspread: Bots Using Service Accounts](https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account)

Follow the instructions in the above link to create an API project in your google account.
Then create a service account. Then create an API key for that service account.
This will generate a `.json` you should save as `credentials.json` in the root of this repo.
