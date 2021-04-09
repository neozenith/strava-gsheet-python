"""Strava API Wrapper.

Simplify the Strava API with a wrapper to abstract only the tasks needed.
"""
# Third Party Libraries
import swagger_client
from swagger_client.rest import ApiException


class StravaAPIWrapper:
    """Simplify the Strava API with a wrapper to abstract only the tasks needed."""

    def __init__(self, client_id, client_secret, access_token, refresh_token):
        """Create StravaAPIWrapper instance with an access token."""
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token

    def list_activities(self, before="", after="", page=1, per_page=30):
        """Extract a list of athlete activities from Strava API."""
        api_response = []

        try:
            api_instance = swagger_client.ActivitiesApi()
            api_instance.api_client.configuration.access_token = self.access_token
            api_response = api_instance.get_logged_in_athlete_activities(
                before=before, after=after, page=page, per_page=per_page
            )
        except ApiException as e:
            print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)

        return [self._filtered_activity(a) for a in api_response]

    def _filtered_activity(self, activity):
        target_attributes = [
            "id",
            "name",
            "start_date_local",
            "moving_time",
            "elapsed_time",
            "type",
            "workout_type" "distance",
            "total_elevation_gain",
            "kilojoules",
            "average_speed",
            "max_speed",
            "average_watts",
            "max_watts",
            "weighted_average_watts",
        ]
        return {attr: getattr(activity, attr) for attr in activity.__dir__() if attr in target_attributes}
