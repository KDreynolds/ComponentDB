# coding: utf-8

"""
    Component Database API

    The API that provides access to Component Database data.  # noqa: E501

    The version of the OpenAPI document: 3.12.3
    Contact: djarosz@anl.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cdbApi.configuration import Configuration


class ApiExceptionMessageExceptionCause(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'stack_trace': 'list[ApiExceptionMessageExceptionCauseStackTrace]',
        'message': 'str',
        'suppressed': 'list[ApiExceptionMessageExceptionCauseSuppressed]',
        'localized_message': 'str'
    }

    attribute_map = {
        'stack_trace': 'stackTrace',
        'message': 'message',
        'suppressed': 'suppressed',
        'localized_message': 'localizedMessage'
    }

    def __init__(self, stack_trace=None, message=None, suppressed=None, localized_message=None, local_vars_configuration=None):  # noqa: E501
        """ApiExceptionMessageExceptionCause - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stack_trace = None
        self._message = None
        self._suppressed = None
        self._localized_message = None
        self.discriminator = None

        if stack_trace is not None:
            self.stack_trace = stack_trace
        if message is not None:
            self.message = message
        if suppressed is not None:
            self.suppressed = suppressed
        if localized_message is not None:
            self.localized_message = localized_message

    @property
    def stack_trace(self):
        """Gets the stack_trace of this ApiExceptionMessageExceptionCause.  # noqa: E501


        :return: The stack_trace of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :rtype: list[ApiExceptionMessageExceptionCauseStackTrace]
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this ApiExceptionMessageExceptionCause.


        :param stack_trace: The stack_trace of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :type: list[ApiExceptionMessageExceptionCauseStackTrace]
        """

        self._stack_trace = stack_trace

    @property
    def message(self):
        """Gets the message of this ApiExceptionMessageExceptionCause.  # noqa: E501


        :return: The message of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiExceptionMessageExceptionCause.


        :param message: The message of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def suppressed(self):
        """Gets the suppressed of this ApiExceptionMessageExceptionCause.  # noqa: E501


        :return: The suppressed of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :rtype: list[ApiExceptionMessageExceptionCauseSuppressed]
        """
        return self._suppressed

    @suppressed.setter
    def suppressed(self, suppressed):
        """Sets the suppressed of this ApiExceptionMessageExceptionCause.


        :param suppressed: The suppressed of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :type: list[ApiExceptionMessageExceptionCauseSuppressed]
        """

        self._suppressed = suppressed

    @property
    def localized_message(self):
        """Gets the localized_message of this ApiExceptionMessageExceptionCause.  # noqa: E501


        :return: The localized_message of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :rtype: str
        """
        return self._localized_message

    @localized_message.setter
    def localized_message(self, localized_message):
        """Sets the localized_message of this ApiExceptionMessageExceptionCause.


        :param localized_message: The localized_message of this ApiExceptionMessageExceptionCause.  # noqa: E501
        :type: str
        """

        self._localized_message = localized_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiExceptionMessageExceptionCause):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiExceptionMessageExceptionCause):
            return True

        return self.to_dict() != other.to_dict()
