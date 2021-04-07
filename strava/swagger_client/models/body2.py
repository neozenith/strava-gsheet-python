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

class Body2(object):
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
        'file': 'str',
        'name': 'str',
        'description': 'str',
        'trainer': 'str',
        'commute': 'str',
        'data_type': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'file': 'file',
        'name': 'name',
        'description': 'description',
        'trainer': 'trainer',
        'commute': 'commute',
        'data_type': 'data_type',
        'external_id': 'external_id'
    }

    def __init__(self, file=None, name=None, description=None, trainer=None, commute=None, data_type=None, external_id=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._name = None
        self._description = None
        self._trainer = None
        self._commute = None
        self._data_type = None
        self._external_id = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if trainer is not None:
            self.trainer = trainer
        if commute is not None:
            self.commute = commute
        if data_type is not None:
            self.data_type = data_type
        if external_id is not None:
            self.external_id = external_id

    @property
    def file(self):
        """Gets the file of this Body2.  # noqa: E501

        The uploaded file.  # noqa: E501

        :return: The file of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Body2.

        The uploaded file.  # noqa: E501

        :param file: The file of this Body2.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def name(self):
        """Gets the name of this Body2.  # noqa: E501

        The desired name of the resulting activity.  # noqa: E501

        :return: The name of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body2.

        The desired name of the resulting activity.  # noqa: E501

        :param name: The name of this Body2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Body2.  # noqa: E501

        The desired description of the resulting activity.  # noqa: E501

        :return: The description of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body2.

        The desired description of the resulting activity.  # noqa: E501

        :param description: The description of this Body2.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def trainer(self):
        """Gets the trainer of this Body2.  # noqa: E501

        Whether the resulting activity should be marked as having been performed on a trainer.  # noqa: E501

        :return: The trainer of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._trainer

    @trainer.setter
    def trainer(self, trainer):
        """Sets the trainer of this Body2.

        Whether the resulting activity should be marked as having been performed on a trainer.  # noqa: E501

        :param trainer: The trainer of this Body2.  # noqa: E501
        :type: str
        """

        self._trainer = trainer

    @property
    def commute(self):
        """Gets the commute of this Body2.  # noqa: E501

        Whether the resulting activity should be tagged as a commute.  # noqa: E501

        :return: The commute of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._commute

    @commute.setter
    def commute(self, commute):
        """Sets the commute of this Body2.

        Whether the resulting activity should be tagged as a commute.  # noqa: E501

        :param commute: The commute of this Body2.  # noqa: E501
        :type: str
        """

        self._commute = commute

    @property
    def data_type(self):
        """Gets the data_type of this Body2.  # noqa: E501

        The format of the uploaded file.  # noqa: E501

        :return: The data_type of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Body2.

        The format of the uploaded file.  # noqa: E501

        :param data_type: The data_type of this Body2.  # noqa: E501
        :type: str
        """
        allowed_values = ["fit", "fit.gz", "tcx", "tcx.gz", "gpx", "gpx.gz"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def external_id(self):
        """Gets the external_id of this Body2.  # noqa: E501

        The desired external identifier of the resulting activity.  # noqa: E501

        :return: The external_id of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Body2.

        The desired external identifier of the resulting activity.  # noqa: E501

        :param external_id: The external_id of this Body2.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(Body2, dict):
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
        if not isinstance(other, Body2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
