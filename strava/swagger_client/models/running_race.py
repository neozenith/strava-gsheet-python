# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RunningRace(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'running_race_type': 'int',
        'distance': 'float',
        'start_date_local': 'datetime',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'route_ids': 'list[int]',
        'measurement_preference': 'str',
        'url': 'str',
        'website_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'running_race_type': 'running_race_type',
        'distance': 'distance',
        'start_date_local': 'start_date_local',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'route_ids': 'route_ids',
        'measurement_preference': 'measurement_preference',
        'url': 'url',
        'website_url': 'website_url'
    }

    def __init__(self, id=None, name=None, running_race_type=None, distance=None, start_date_local=None, city=None, state=None, country=None, route_ids=None, measurement_preference=None, url=None, website_url=None):  # noqa: E501
        """RunningRace - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._running_race_type = None
        self._distance = None
        self._start_date_local = None
        self._city = None
        self._state = None
        self._country = None
        self._route_ids = None
        self._measurement_preference = None
        self._url = None
        self._website_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if running_race_type is not None:
            self.running_race_type = running_race_type
        if distance is not None:
            self.distance = distance
        if start_date_local is not None:
            self.start_date_local = start_date_local
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if route_ids is not None:
            self.route_ids = route_ids
        if measurement_preference is not None:
            self.measurement_preference = measurement_preference
        if url is not None:
            self.url = url
        if website_url is not None:
            self.website_url = website_url

    @property
    def id(self):
        """Gets the id of this RunningRace.  # noqa: E501

        The unique identifier of this race.  # noqa: E501

        :return: The id of this RunningRace.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunningRace.

        The unique identifier of this race.  # noqa: E501

        :param id: The id of this RunningRace.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RunningRace.  # noqa: E501

        The name of this race.  # noqa: E501

        :return: The name of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RunningRace.

        The name of this race.  # noqa: E501

        :param name: The name of this RunningRace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def running_race_type(self):
        """Gets the running_race_type of this RunningRace.  # noqa: E501

        The type of this race.  # noqa: E501

        :return: The running_race_type of this RunningRace.  # noqa: E501
        :rtype: int
        """
        return self._running_race_type

    @running_race_type.setter
    def running_race_type(self, running_race_type):
        """Sets the running_race_type of this RunningRace.

        The type of this race.  # noqa: E501

        :param running_race_type: The running_race_type of this RunningRace.  # noqa: E501
        :type: int
        """

        self._running_race_type = running_race_type

    @property
    def distance(self):
        """Gets the distance of this RunningRace.  # noqa: E501

        The race's distance, in meters.  # noqa: E501

        :return: The distance of this RunningRace.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RunningRace.

        The race's distance, in meters.  # noqa: E501

        :param distance: The distance of this RunningRace.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def start_date_local(self):
        """Gets the start_date_local of this RunningRace.  # noqa: E501

        The time at which the race begins started in the local timezone.  # noqa: E501

        :return: The start_date_local of this RunningRace.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_local

    @start_date_local.setter
    def start_date_local(self, start_date_local):
        """Sets the start_date_local of this RunningRace.

        The time at which the race begins started in the local timezone.  # noqa: E501

        :param start_date_local: The start_date_local of this RunningRace.  # noqa: E501
        :type: datetime
        """

        self._start_date_local = start_date_local

    @property
    def city(self):
        """Gets the city of this RunningRace.  # noqa: E501

        The name of the city in which the race is taking place.  # noqa: E501

        :return: The city of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this RunningRace.

        The name of the city in which the race is taking place.  # noqa: E501

        :param city: The city of this RunningRace.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this RunningRace.  # noqa: E501

        The name of the state or geographical region in which the race is taking place.  # noqa: E501

        :return: The state of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RunningRace.

        The name of the state or geographical region in which the race is taking place.  # noqa: E501

        :param state: The state of this RunningRace.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this RunningRace.  # noqa: E501

        The name of the country in which the race is taking place.  # noqa: E501

        :return: The country of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this RunningRace.

        The name of the country in which the race is taking place.  # noqa: E501

        :param country: The country of this RunningRace.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def route_ids(self):
        """Gets the route_ids of this RunningRace.  # noqa: E501

        The set of routes that cover this race's course.  # noqa: E501

        :return: The route_ids of this RunningRace.  # noqa: E501
        :rtype: list[int]
        """
        return self._route_ids

    @route_ids.setter
    def route_ids(self, route_ids):
        """Sets the route_ids of this RunningRace.

        The set of routes that cover this race's course.  # noqa: E501

        :param route_ids: The route_ids of this RunningRace.  # noqa: E501
        :type: list[int]
        """

        self._route_ids = route_ids

    @property
    def measurement_preference(self):
        """Gets the measurement_preference of this RunningRace.  # noqa: E501

        The unit system in which the race should be displayed.  # noqa: E501

        :return: The measurement_preference of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._measurement_preference

    @measurement_preference.setter
    def measurement_preference(self, measurement_preference):
        """Sets the measurement_preference of this RunningRace.

        The unit system in which the race should be displayed.  # noqa: E501

        :param measurement_preference: The measurement_preference of this RunningRace.  # noqa: E501
        :type: str
        """
        allowed_values = ["feet", "meters"]  # noqa: E501
        if measurement_preference not in allowed_values:
            raise ValueError(
                "Invalid value for `measurement_preference` ({0}), must be one of {1}"  # noqa: E501
                .format(measurement_preference, allowed_values)
            )

        self._measurement_preference = measurement_preference

    @property
    def url(self):
        """Gets the url of this RunningRace.  # noqa: E501

        The vanity URL of this race on Strava.  # noqa: E501

        :return: The url of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RunningRace.

        The vanity URL of this race on Strava.  # noqa: E501

        :param url: The url of this RunningRace.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def website_url(self):
        """Gets the website_url of this RunningRace.  # noqa: E501

        The URL of this race's website.  # noqa: E501

        :return: The website_url of this RunningRace.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this RunningRace.

        The URL of this race's website.  # noqa: E501

        :param website_url: The website_url of this RunningRace.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RunningRace, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunningRace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
