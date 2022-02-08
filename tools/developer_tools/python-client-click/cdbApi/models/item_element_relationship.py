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


class ItemElementRelationship(object):
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
        'property_value_list': 'list[PropertyValue]',
        'item_element_relationship_history_list': 'list[ItemElementRelationshipHistory]',
        'first_item_element': 'ItemElement',
        'first_item_connector': 'ItemConnector',
        'first_sort_order': 'float',
        'second_item_element': 'ItemElement',
        'second_item_connector': 'ItemConnector',
        'second_sort_order': 'float',
        'relationship_type': 'RelationshipType',
        'link_item_element': 'ItemElement',
        'resource_type': 'ResourceType',
        'import_first_item': 'Item',
        'import_second_item': 'Item',
        'import_first_item_connector_name': 'str',
        'import_second_item_connector_name': 'str',
        'import_primary_cable_connection': 'bool',
        'primary_cable_connection': 'bool',
        'first_item': 'Item',
        'first_item_connector_name': 'str',
        'second_item': 'Item',
        'second_item_connector_name': 'str',
        'cable_end_primary_indicator': 'str',
        'cable_end_primary_sort_value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'relationship_details': 'relationshipDetails',
        'label': 'label',
        'description': 'description',
        'property_value_list': 'propertyValueList',
        'item_element_relationship_history_list': 'itemElementRelationshipHistoryList',
        'first_item_element': 'firstItemElement',
        'first_item_connector': 'firstItemConnector',
        'first_sort_order': 'firstSortOrder',
        'second_item_element': 'secondItemElement',
        'second_item_connector': 'secondItemConnector',
        'second_sort_order': 'secondSortOrder',
        'relationship_type': 'relationshipType',
        'link_item_element': 'linkItemElement',
        'resource_type': 'resourceType',
        'import_first_item': 'importFirstItem',
        'import_second_item': 'importSecondItem',
        'import_first_item_connector_name': 'importFirstItemConnectorName',
        'import_second_item_connector_name': 'importSecondItemConnectorName',
        'import_primary_cable_connection': 'importPrimaryCableConnection',
        'primary_cable_connection': 'primaryCableConnection',
        'first_item': 'firstItem',
        'first_item_connector_name': 'firstItemConnectorName',
        'second_item': 'secondItem',
        'second_item_connector_name': 'secondItemConnectorName',
        'cable_end_primary_indicator': 'cableEndPrimaryIndicator',
        'cable_end_primary_sort_value': 'cableEndPrimarySortValue'
    }

    def __init__(self, id=None, relationship_details=None, label=None, description=None, property_value_list=None, item_element_relationship_history_list=None, first_item_element=None, first_item_connector=None, first_sort_order=None, second_item_element=None, second_item_connector=None, second_sort_order=None, relationship_type=None, link_item_element=None, resource_type=None, import_first_item=None, import_second_item=None, import_first_item_connector_name=None, import_second_item_connector_name=None, import_primary_cable_connection=None, primary_cable_connection=None, first_item=None, first_item_connector_name=None, second_item=None, second_item_connector_name=None, cable_end_primary_indicator=None, cable_end_primary_sort_value=None, local_vars_configuration=None):  # noqa: E501
        """ItemElementRelationship - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._relationship_details = None
        self._label = None
        self._description = None
        self._property_value_list = None
        self._item_element_relationship_history_list = None
        self._first_item_element = None
        self._first_item_connector = None
        self._first_sort_order = None
        self._second_item_element = None
        self._second_item_connector = None
        self._second_sort_order = None
        self._relationship_type = None
        self._link_item_element = None
        self._resource_type = None
        self._import_first_item = None
        self._import_second_item = None
        self._import_first_item_connector_name = None
        self._import_second_item_connector_name = None
        self._import_primary_cable_connection = None
        self._primary_cable_connection = None
        self._first_item = None
        self._first_item_connector_name = None
        self._second_item = None
        self._second_item_connector_name = None
        self._cable_end_primary_indicator = None
        self._cable_end_primary_sort_value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if relationship_details is not None:
            self.relationship_details = relationship_details
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if property_value_list is not None:
            self.property_value_list = property_value_list
        if item_element_relationship_history_list is not None:
            self.item_element_relationship_history_list = item_element_relationship_history_list
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
        if relationship_type is not None:
            self.relationship_type = relationship_type
        if link_item_element is not None:
            self.link_item_element = link_item_element
        if resource_type is not None:
            self.resource_type = resource_type
        if import_first_item is not None:
            self.import_first_item = import_first_item
        if import_second_item is not None:
            self.import_second_item = import_second_item
        if import_first_item_connector_name is not None:
            self.import_first_item_connector_name = import_first_item_connector_name
        if import_second_item_connector_name is not None:
            self.import_second_item_connector_name = import_second_item_connector_name
        if import_primary_cable_connection is not None:
            self.import_primary_cable_connection = import_primary_cable_connection
        if primary_cable_connection is not None:
            self.primary_cable_connection = primary_cable_connection
        if first_item is not None:
            self.first_item = first_item
        if first_item_connector_name is not None:
            self.first_item_connector_name = first_item_connector_name
        if second_item is not None:
            self.second_item = second_item
        if second_item_connector_name is not None:
            self.second_item_connector_name = second_item_connector_name
        if cable_end_primary_indicator is not None:
            self.cable_end_primary_indicator = cable_end_primary_indicator
        if cable_end_primary_sort_value is not None:
            self.cable_end_primary_sort_value = cable_end_primary_sort_value

    @property
    def id(self):
        """Gets the id of this ItemElementRelationship.  # noqa: E501


        :return: The id of this ItemElementRelationship.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemElementRelationship.


        :param id: The id of this ItemElementRelationship.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def relationship_details(self):
        """Gets the relationship_details of this ItemElementRelationship.  # noqa: E501


        :return: The relationship_details of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._relationship_details

    @relationship_details.setter
    def relationship_details(self, relationship_details):
        """Sets the relationship_details of this ItemElementRelationship.


        :param relationship_details: The relationship_details of this ItemElementRelationship.  # noqa: E501
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
        """Gets the label of this ItemElementRelationship.  # noqa: E501


        :return: The label of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ItemElementRelationship.


        :param label: The label of this ItemElementRelationship.  # noqa: E501
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
        """Gets the description of this ItemElementRelationship.  # noqa: E501


        :return: The description of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ItemElementRelationship.


        :param description: The description of this ItemElementRelationship.  # noqa: E501
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
    def property_value_list(self):
        """Gets the property_value_list of this ItemElementRelationship.  # noqa: E501


        :return: The property_value_list of this ItemElementRelationship.  # noqa: E501
        :rtype: list[PropertyValue]
        """
        return self._property_value_list

    @property_value_list.setter
    def property_value_list(self, property_value_list):
        """Sets the property_value_list of this ItemElementRelationship.


        :param property_value_list: The property_value_list of this ItemElementRelationship.  # noqa: E501
        :type: list[PropertyValue]
        """

        self._property_value_list = property_value_list

    @property
    def item_element_relationship_history_list(self):
        """Gets the item_element_relationship_history_list of this ItemElementRelationship.  # noqa: E501


        :return: The item_element_relationship_history_list of this ItemElementRelationship.  # noqa: E501
        :rtype: list[ItemElementRelationshipHistory]
        """
        return self._item_element_relationship_history_list

    @item_element_relationship_history_list.setter
    def item_element_relationship_history_list(self, item_element_relationship_history_list):
        """Sets the item_element_relationship_history_list of this ItemElementRelationship.


        :param item_element_relationship_history_list: The item_element_relationship_history_list of this ItemElementRelationship.  # noqa: E501
        :type: list[ItemElementRelationshipHistory]
        """

        self._item_element_relationship_history_list = item_element_relationship_history_list

    @property
    def first_item_element(self):
        """Gets the first_item_element of this ItemElementRelationship.  # noqa: E501


        :return: The first_item_element of this ItemElementRelationship.  # noqa: E501
        :rtype: ItemElement
        """
        return self._first_item_element

    @first_item_element.setter
    def first_item_element(self, first_item_element):
        """Sets the first_item_element of this ItemElementRelationship.


        :param first_item_element: The first_item_element of this ItemElementRelationship.  # noqa: E501
        :type: ItemElement
        """

        self._first_item_element = first_item_element

    @property
    def first_item_connector(self):
        """Gets the first_item_connector of this ItemElementRelationship.  # noqa: E501


        :return: The first_item_connector of this ItemElementRelationship.  # noqa: E501
        :rtype: ItemConnector
        """
        return self._first_item_connector

    @first_item_connector.setter
    def first_item_connector(self, first_item_connector):
        """Sets the first_item_connector of this ItemElementRelationship.


        :param first_item_connector: The first_item_connector of this ItemElementRelationship.  # noqa: E501
        :type: ItemConnector
        """

        self._first_item_connector = first_item_connector

    @property
    def first_sort_order(self):
        """Gets the first_sort_order of this ItemElementRelationship.  # noqa: E501


        :return: The first_sort_order of this ItemElementRelationship.  # noqa: E501
        :rtype: float
        """
        return self._first_sort_order

    @first_sort_order.setter
    def first_sort_order(self, first_sort_order):
        """Sets the first_sort_order of this ItemElementRelationship.


        :param first_sort_order: The first_sort_order of this ItemElementRelationship.  # noqa: E501
        :type: float
        """

        self._first_sort_order = first_sort_order

    @property
    def second_item_element(self):
        """Gets the second_item_element of this ItemElementRelationship.  # noqa: E501


        :return: The second_item_element of this ItemElementRelationship.  # noqa: E501
        :rtype: ItemElement
        """
        return self._second_item_element

    @second_item_element.setter
    def second_item_element(self, second_item_element):
        """Sets the second_item_element of this ItemElementRelationship.


        :param second_item_element: The second_item_element of this ItemElementRelationship.  # noqa: E501
        :type: ItemElement
        """

        self._second_item_element = second_item_element

    @property
    def second_item_connector(self):
        """Gets the second_item_connector of this ItemElementRelationship.  # noqa: E501


        :return: The second_item_connector of this ItemElementRelationship.  # noqa: E501
        :rtype: ItemConnector
        """
        return self._second_item_connector

    @second_item_connector.setter
    def second_item_connector(self, second_item_connector):
        """Sets the second_item_connector of this ItemElementRelationship.


        :param second_item_connector: The second_item_connector of this ItemElementRelationship.  # noqa: E501
        :type: ItemConnector
        """

        self._second_item_connector = second_item_connector

    @property
    def second_sort_order(self):
        """Gets the second_sort_order of this ItemElementRelationship.  # noqa: E501


        :return: The second_sort_order of this ItemElementRelationship.  # noqa: E501
        :rtype: float
        """
        return self._second_sort_order

    @second_sort_order.setter
    def second_sort_order(self, second_sort_order):
        """Sets the second_sort_order of this ItemElementRelationship.


        :param second_sort_order: The second_sort_order of this ItemElementRelationship.  # noqa: E501
        :type: float
        """

        self._second_sort_order = second_sort_order

    @property
    def relationship_type(self):
        """Gets the relationship_type of this ItemElementRelationship.  # noqa: E501


        :return: The relationship_type of this ItemElementRelationship.  # noqa: E501
        :rtype: RelationshipType
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """Sets the relationship_type of this ItemElementRelationship.


        :param relationship_type: The relationship_type of this ItemElementRelationship.  # noqa: E501
        :type: RelationshipType
        """

        self._relationship_type = relationship_type

    @property
    def link_item_element(self):
        """Gets the link_item_element of this ItemElementRelationship.  # noqa: E501


        :return: The link_item_element of this ItemElementRelationship.  # noqa: E501
        :rtype: ItemElement
        """
        return self._link_item_element

    @link_item_element.setter
    def link_item_element(self, link_item_element):
        """Sets the link_item_element of this ItemElementRelationship.


        :param link_item_element: The link_item_element of this ItemElementRelationship.  # noqa: E501
        :type: ItemElement
        """

        self._link_item_element = link_item_element

    @property
    def resource_type(self):
        """Gets the resource_type of this ItemElementRelationship.  # noqa: E501


        :return: The resource_type of this ItemElementRelationship.  # noqa: E501
        :rtype: ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ItemElementRelationship.


        :param resource_type: The resource_type of this ItemElementRelationship.  # noqa: E501
        :type: ResourceType
        """

        self._resource_type = resource_type

    @property
    def import_first_item(self):
        """Gets the import_first_item of this ItemElementRelationship.  # noqa: E501


        :return: The import_first_item of this ItemElementRelationship.  # noqa: E501
        :rtype: Item
        """
        return self._import_first_item

    @import_first_item.setter
    def import_first_item(self, import_first_item):
        """Sets the import_first_item of this ItemElementRelationship.


        :param import_first_item: The import_first_item of this ItemElementRelationship.  # noqa: E501
        :type: Item
        """

        self._import_first_item = import_first_item

    @property
    def import_second_item(self):
        """Gets the import_second_item of this ItemElementRelationship.  # noqa: E501


        :return: The import_second_item of this ItemElementRelationship.  # noqa: E501
        :rtype: Item
        """
        return self._import_second_item

    @import_second_item.setter
    def import_second_item(self, import_second_item):
        """Sets the import_second_item of this ItemElementRelationship.


        :param import_second_item: The import_second_item of this ItemElementRelationship.  # noqa: E501
        :type: Item
        """

        self._import_second_item = import_second_item

    @property
    def import_first_item_connector_name(self):
        """Gets the import_first_item_connector_name of this ItemElementRelationship.  # noqa: E501


        :return: The import_first_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._import_first_item_connector_name

    @import_first_item_connector_name.setter
    def import_first_item_connector_name(self, import_first_item_connector_name):
        """Sets the import_first_item_connector_name of this ItemElementRelationship.


        :param import_first_item_connector_name: The import_first_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._import_first_item_connector_name = import_first_item_connector_name

    @property
    def import_second_item_connector_name(self):
        """Gets the import_second_item_connector_name of this ItemElementRelationship.  # noqa: E501


        :return: The import_second_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._import_second_item_connector_name

    @import_second_item_connector_name.setter
    def import_second_item_connector_name(self, import_second_item_connector_name):
        """Sets the import_second_item_connector_name of this ItemElementRelationship.


        :param import_second_item_connector_name: The import_second_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._import_second_item_connector_name = import_second_item_connector_name

    @property
    def import_primary_cable_connection(self):
        """Gets the import_primary_cable_connection of this ItemElementRelationship.  # noqa: E501


        :return: The import_primary_cable_connection of this ItemElementRelationship.  # noqa: E501
        :rtype: bool
        """
        return self._import_primary_cable_connection

    @import_primary_cable_connection.setter
    def import_primary_cable_connection(self, import_primary_cable_connection):
        """Sets the import_primary_cable_connection of this ItemElementRelationship.


        :param import_primary_cable_connection: The import_primary_cable_connection of this ItemElementRelationship.  # noqa: E501
        :type: bool
        """

        self._import_primary_cable_connection = import_primary_cable_connection

    @property
    def primary_cable_connection(self):
        """Gets the primary_cable_connection of this ItemElementRelationship.  # noqa: E501


        :return: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
        :rtype: bool
        """
        return self._primary_cable_connection

    @primary_cable_connection.setter
    def primary_cable_connection(self, primary_cable_connection):
        """Sets the primary_cable_connection of this ItemElementRelationship.


        :param primary_cable_connection: The primary_cable_connection of this ItemElementRelationship.  # noqa: E501
        :type: bool
        """

        self._primary_cable_connection = primary_cable_connection

    @property
    def first_item(self):
        """Gets the first_item of this ItemElementRelationship.  # noqa: E501


        :return: The first_item of this ItemElementRelationship.  # noqa: E501
        :rtype: Item
        """
        return self._first_item

    @first_item.setter
    def first_item(self, first_item):
        """Sets the first_item of this ItemElementRelationship.


        :param first_item: The first_item of this ItemElementRelationship.  # noqa: E501
        :type: Item
        """

        self._first_item = first_item

    @property
    def first_item_connector_name(self):
        """Gets the first_item_connector_name of this ItemElementRelationship.  # noqa: E501


        :return: The first_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._first_item_connector_name

    @first_item_connector_name.setter
    def first_item_connector_name(self, first_item_connector_name):
        """Sets the first_item_connector_name of this ItemElementRelationship.


        :param first_item_connector_name: The first_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._first_item_connector_name = first_item_connector_name

    @property
    def second_item(self):
        """Gets the second_item of this ItemElementRelationship.  # noqa: E501


        :return: The second_item of this ItemElementRelationship.  # noqa: E501
        :rtype: Item
        """
        return self._second_item

    @second_item.setter
    def second_item(self, second_item):
        """Sets the second_item of this ItemElementRelationship.


        :param second_item: The second_item of this ItemElementRelationship.  # noqa: E501
        :type: Item
        """

        self._second_item = second_item

    @property
    def second_item_connector_name(self):
        """Gets the second_item_connector_name of this ItemElementRelationship.  # noqa: E501


        :return: The second_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._second_item_connector_name

    @second_item_connector_name.setter
    def second_item_connector_name(self, second_item_connector_name):
        """Sets the second_item_connector_name of this ItemElementRelationship.


        :param second_item_connector_name: The second_item_connector_name of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._second_item_connector_name = second_item_connector_name

    @property
    def cable_end_primary_indicator(self):
        """Gets the cable_end_primary_indicator of this ItemElementRelationship.  # noqa: E501


        :return: The cable_end_primary_indicator of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._cable_end_primary_indicator

    @cable_end_primary_indicator.setter
    def cable_end_primary_indicator(self, cable_end_primary_indicator):
        """Sets the cable_end_primary_indicator of this ItemElementRelationship.


        :param cable_end_primary_indicator: The cable_end_primary_indicator of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._cable_end_primary_indicator = cable_end_primary_indicator

    @property
    def cable_end_primary_sort_value(self):
        """Gets the cable_end_primary_sort_value of this ItemElementRelationship.  # noqa: E501


        :return: The cable_end_primary_sort_value of this ItemElementRelationship.  # noqa: E501
        :rtype: str
        """
        return self._cable_end_primary_sort_value

    @cable_end_primary_sort_value.setter
    def cable_end_primary_sort_value(self, cable_end_primary_sort_value):
        """Sets the cable_end_primary_sort_value of this ItemElementRelationship.


        :param cable_end_primary_sort_value: The cable_end_primary_sort_value of this ItemElementRelationship.  # noqa: E501
        :type: str
        """

        self._cable_end_primary_sort_value = cable_end_primary_sort_value

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
        if not isinstance(other, ItemElementRelationship):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemElementRelationship):
            return True

        return self.to_dict() != other.to_dict()
