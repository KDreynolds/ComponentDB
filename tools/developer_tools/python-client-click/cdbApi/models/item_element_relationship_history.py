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


class ItemElementRelationshipHistory(object):
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
        'id': 'int',
        'relationship_details': 'str',
        'label': 'str',
        'description': 'str',
        'entered_on_date_time': 'datetime',
        'item_element_relationship': 'ItemElementRelationship',
        'first_item_element': 'ItemElement',
        'first_item_connector': 'ItemConnector',
        'first_sort_order': 'float',
        'second_item_element': 'ItemElement',
        'second_item_connector': 'ItemConnector',
        'second_sort_order': 'float',
        'link_item_element': 'ItemElement',
        'resource_type': 'ResourceType',
        'entered_by_user': 'UserInfo'
    }

    attribute_map = {
        'id': 'id',
        'relationship_details': 'relationshipDetails',
        'label': 'label',
        'description': 'description',
        'entered_on_date_time': 'enteredOnDateTime',
        'item_element_relationship': 'itemElementRelationship',
        'first_item_element': 'firstItemElement',
        'first_item_connector': 'firstItemConnector',
        'first_sort_order': 'firstSortOrder',
        'second_item_element': 'secondItemElement',
        'second_item_connector': 'secondItemConnector',
        'second_sort_order': 'secondSortOrder',
        'link_item_element': 'linkItemElement',
        'resource_type': 'resourceType',
        'entered_by_user': 'enteredByUser'
    }

    def __init__(self, id=None, relationship_details=None, label=None, description=None, entered_on_date_time=None, item_element_relationship=None, first_item_element=None, first_item_connector=None, first_sort_order=None, second_item_element=None, second_item_connector=None, second_sort_order=None, link_item_element=None, resource_type=None, entered_by_user=None, local_vars_configuration=None):  # noqa: E501
        """ItemElementRelationshipHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._relationship_details = None
        self._label = None
        self._description = None
        self._entered_on_date_time = None
        self._item_element_relationship = None
        self._first_item_element = None
        self._first_item_connector = None
        self._first_sort_order = None
        self._second_item_element = None
        self._second_item_connector = None
        self._second_sort_order = None
        self._link_item_element = None
        self._resource_type = None
        self._entered_by_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if relationship_details is not None:
            self.relationship_details = relationship_details
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        self.entered_on_date_time = entered_on_date_time
        if item_element_relationship is not None:
            self.item_element_relationship = item_element_relationship
        if first_item_element is not None:
            self.first_item_element = first_item_element
        if first_item_connector is not None:
            self.first_item_connector = first_item_connector
        if first_sort_order is not None:
            self.first_sort_order = first_sort_order
        if second_item_element is not None:
            self.second_item_element = second_item_element
        if second_item_connector is not None:
            self.second_item_connector = second_item_connector
        if second_sort_order is not None:
            self.second_sort_order = second_sort_order
        if link_item_element is not None:
            self.link_item_element = link_item_element
        if resource_type is not None:
            self.resource_type = resource_type
        if entered_by_user is not None:
            self.entered_by_user = entered_by_user

    @property
    def id(self):
        """Gets the id of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The id of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemElementRelationshipHistory.


        :param id: The id of this ItemElementRelationshipHistory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def relationship_details(self):
        """Gets the relationship_details of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The relationship_details of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: str
        """
        return self._relationship_details

    @relationship_details.setter
    def relationship_details(self, relationship_details):
        """Sets the relationship_details of this ItemElementRelationshipHistory.


        :param relationship_details: The relationship_details of this ItemElementRelationshipHistory.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                relationship_details is not None and len(relationship_details) > 64):
            raise ValueError("Invalid value for `relationship_details`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relationship_details is not None and len(relationship_details) < 0):
            raise ValueError("Invalid value for `relationship_details`, length must be greater than or equal to `0`")  # noqa: E501

        self._relationship_details = relationship_details

    @property
    def label(self):
        """Gets the label of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The label of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ItemElementRelationshipHistory.


        :param label: The label of this ItemElementRelationshipHistory.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) > 64):
            raise ValueError("Invalid value for `label`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                label is not None and len(label) < 0):
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `0`")  # noqa: E501

        self._label = label

    @property
    def description(self):
        """Gets the description of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The description of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemElementRelationshipHistory.


        :param description: The description of this ItemElementRelationshipHistory.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 256):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def entered_on_date_time(self):
        """Gets the entered_on_date_time of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The entered_on_date_time of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._entered_on_date_time

    @entered_on_date_time.setter
    def entered_on_date_time(self, entered_on_date_time):
        """Sets the entered_on_date_time of this ItemElementRelationshipHistory.


        :param entered_on_date_time: The entered_on_date_time of this ItemElementRelationshipHistory.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and entered_on_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `entered_on_date_time`, must not be `None`")  # noqa: E501

        self._entered_on_date_time = entered_on_date_time

    @property
    def item_element_relationship(self):
        """Gets the item_element_relationship of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The item_element_relationship of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemElementRelationship
        """
        return self._item_element_relationship

    @item_element_relationship.setter
    def item_element_relationship(self, item_element_relationship):
        """Sets the item_element_relationship of this ItemElementRelationshipHistory.


        :param item_element_relationship: The item_element_relationship of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemElementRelationship
        """

        self._item_element_relationship = item_element_relationship

    @property
    def first_item_element(self):
        """Gets the first_item_element of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The first_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemElement
        """
        return self._first_item_element

    @first_item_element.setter
    def first_item_element(self, first_item_element):
        """Sets the first_item_element of this ItemElementRelationshipHistory.


        :param first_item_element: The first_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemElement
        """

        self._first_item_element = first_item_element

    @property
    def first_item_connector(self):
        """Gets the first_item_connector of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The first_item_connector of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemConnector
        """
        return self._first_item_connector

    @first_item_connector.setter
    def first_item_connector(self, first_item_connector):
        """Sets the first_item_connector of this ItemElementRelationshipHistory.


        :param first_item_connector: The first_item_connector of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemConnector
        """

        self._first_item_connector = first_item_connector

    @property
    def first_sort_order(self):
        """Gets the first_sort_order of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The first_sort_order of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: float
        """
        return self._first_sort_order

    @first_sort_order.setter
    def first_sort_order(self, first_sort_order):
        """Sets the first_sort_order of this ItemElementRelationshipHistory.


        :param first_sort_order: The first_sort_order of this ItemElementRelationshipHistory.  # noqa: E501
        :type: float
        """

        self._first_sort_order = first_sort_order

    @property
    def second_item_element(self):
        """Gets the second_item_element of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The second_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemElement
        """
        return self._second_item_element

    @second_item_element.setter
    def second_item_element(self, second_item_element):
        """Sets the second_item_element of this ItemElementRelationshipHistory.


        :param second_item_element: The second_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemElement
        """

        self._second_item_element = second_item_element

    @property
    def second_item_connector(self):
        """Gets the second_item_connector of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The second_item_connector of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemConnector
        """
        return self._second_item_connector

    @second_item_connector.setter
    def second_item_connector(self, second_item_connector):
        """Sets the second_item_connector of this ItemElementRelationshipHistory.


        :param second_item_connector: The second_item_connector of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemConnector
        """

        self._second_item_connector = second_item_connector

    @property
    def second_sort_order(self):
        """Gets the second_sort_order of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The second_sort_order of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: float
        """
        return self._second_sort_order

    @second_sort_order.setter
    def second_sort_order(self, second_sort_order):
        """Sets the second_sort_order of this ItemElementRelationshipHistory.


        :param second_sort_order: The second_sort_order of this ItemElementRelationshipHistory.  # noqa: E501
        :type: float
        """

        self._second_sort_order = second_sort_order

    @property
    def link_item_element(self):
        """Gets the link_item_element of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The link_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ItemElement
        """
        return self._link_item_element

    @link_item_element.setter
    def link_item_element(self, link_item_element):
        """Sets the link_item_element of this ItemElementRelationshipHistory.


        :param link_item_element: The link_item_element of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ItemElement
        """

        self._link_item_element = link_item_element

    @property
    def resource_type(self):
        """Gets the resource_type of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The resource_type of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ItemElementRelationshipHistory.


        :param resource_type: The resource_type of this ItemElementRelationshipHistory.  # noqa: E501
        :type: ResourceType
        """

        self._resource_type = resource_type

    @property
    def entered_by_user(self):
        """Gets the entered_by_user of this ItemElementRelationshipHistory.  # noqa: E501


        :return: The entered_by_user of this ItemElementRelationshipHistory.  # noqa: E501
        :rtype: UserInfo
        """
        return self._entered_by_user

    @entered_by_user.setter
    def entered_by_user(self, entered_by_user):
        """Sets the entered_by_user of this ItemElementRelationshipHistory.


        :param entered_by_user: The entered_by_user of this ItemElementRelationshipHistory.  # noqa: E501
        :type: UserInfo
        """

        self._entered_by_user = entered_by_user

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
        if not isinstance(other, ItemElementRelationshipHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemElementRelationshipHistory):
            return True

        return self.to_dict() != other.to_dict()
