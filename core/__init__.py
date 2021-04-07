# Standard Library
import os
import time
from pprint import pprint

# Third Party Libraries
import swagger_client
from dotenv import load_dotenv
from swagger_client.rest import ApiException

load_dotenv()


def list_activities(page=1, perPage=30):
    api_response = None

    try:
        api_instance = swagger_client.ActivitiesApi()
        api_instance.api_client.configuration.access_token = os.getenv("STRAVA_ACCESS_TOKEN")
        api_response = api_instance.get_logged_in_athlete_activities(page=page, per_page=perPage)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)

    return api_response
