"""Strava API Wrapper.

Simplify the Strava API with a wrapper to abstract only the tasks needed.
"""
# Third Party Libraries
import swagger_client
from swagger_client.rest import ApiException


class StravaAPIWrapper:
    """Simplify the Strava API with a wrapper to abstract only the tasks needed."""

    def __init__(self, access_token):
        """Create StravaAPIWrapper instance with an access token."""
        super().__init__()
        self.access_token = access_token

    def list_activities(self, page=1, perPage=30):
        """Extract a list of athlete activities from Strava API."""
        api_response = None

        try:
            api_instance = swagger_client.ActivitiesApi()
            api_instance.api_client.configuration.access_token = self.access_token
            api_response = api_instance.get_logged_in_athlete_activities(page=page, per_page=perPage)
        except ApiException as e:
            print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)

        return api_response
