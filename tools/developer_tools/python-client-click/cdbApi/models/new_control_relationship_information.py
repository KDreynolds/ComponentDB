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


class NewControlRelationshipInformation(object):
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
        'controlled_machine_id': 'int',
        'controlling_machine_id': 'int',
        'control_interface_to_parent': 'str'
    }

    attribute_map = {
        'controlled_machine_id': 'controlledMachineId',
        'controlling_machine_id': 'controllingMachineId',
        'control_interface_to_parent': 'controlInterfaceToParent'
    }

    def __init__(self, controlled_machine_id=None, controlling_machine_id=None, control_interface_to_parent=None, local_vars_configuration=None):  # noqa: E501
        """NewControlRelationshipInformation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._controlled_machine_id = None
        self._controlling_machine_id = None
        self._control_interface_to_parent = None
        self.discriminator = None

        if controlled_machine_id is not None:
            self.controlled_machine_id = controlled_machine_id
        if controlling_machine_id is not None:
            self.controlling_machine_id = controlling_machine_id
        if control_interface_to_parent is not None:
            self.control_interface_to_parent = control_interface_to_parent

    @property
    def controlled_machine_id(self):
        """Gets the controlled_machine_id of this NewControlRelationshipInformation.  # noqa: E501


        :return: The controlled_machine_id of this NewControlRelationshipInformation.  # noqa: E501
        :rtype: int
        """
        return self._controlled_machine_id

    @controlled_machine_id.setter
    def controlled_machine_id(self, controlled_machine_id):
        """Sets the controlled_machine_id of this NewControlRelationshipInformation.


        :param controlled_machine_id: The controlled_machine_id of this NewControlRelationshipInformation.  # noqa: E501
        :type: int
        """

        self._controlled_machine_id = controlled_machine_id

    @property
    def controlling_machine_id(self):
        """Gets the controlling_machine_id of this NewControlRelationshipInformation.  # noqa: E501


        :return: The controlling_machine_id of this NewControlRelationshipInformation.  # noqa: E501
        :rtype: int
        """
        return self._controlling_machine_id

    @controlling_machine_id.setter
    def controlling_machine_id(self, controlling_machine_id):
        """Sets the controlling_machine_id of this NewControlRelationshipInformation.


        :param controlling_machine_id: The controlling_machine_id of this NewControlRelationshipInformation.  # noqa: E501
        :type: int
        """

        self._controlling_machine_id = controlling_machine_id

    @property
    def control_interface_to_parent(self):
        """Gets the control_interface_to_parent of this NewControlRelationshipInformation.  # noqa: E501


        :return: The control_interface_to_parent of this NewControlRelationshipInformation.  # noqa: E501
        :rtype: str
        """
        return self._control_interface_to_parent

    @control_interface_to_parent.setter
    def control_interface_to_parent(self, control_interface_to_parent):
        """Sets the control_interface_to_parent of this NewControlRelationshipInformation.


        :param control_interface_to_parent: The control_interface_to_parent of this NewControlRelationshipInformation.  # noqa: E501
        :type: str
        """

        self._control_interface_to_parent = control_interface_to_parent

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
        if not isinstance(other, NewControlRelationshipInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewControlRelationshipInformation):
            return True

        return self.to_dict() != other.to_dict()
