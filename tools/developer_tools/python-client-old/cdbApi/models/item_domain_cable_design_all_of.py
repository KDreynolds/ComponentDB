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


class ItemDomainCableDesignAllOf(object):
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
        'alternate_name': 'str',
        'catalog_item': 'Item',
        'technical_system_list': 'list[ItemCategory]',
        'catalog_item_id': 'str',
        'catalog_item_string': 'str'
    }

    attribute_map = {
        'alternate_name': 'alternateName',
        'catalog_item': 'catalogItem',
        'technical_system_list': 'technicalSystemList',
        'catalog_item_id': 'catalogItemId',
        'catalog_item_string': 'catalogItemString'
    }

    def __init__(self, alternate_name=None, catalog_item=None, technical_system_list=None, catalog_item_id=None, catalog_item_string=None, local_vars_configuration=None):  # noqa: E501
        """ItemDomainCableDesignAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alternate_name = None
        self._catalog_item = None
        self._technical_system_list = None
        self._catalog_item_id = None
        self._catalog_item_string = None
        self.discriminator = None

        if alternate_name is not None:
            self.alternate_name = alternate_name
        if catalog_item is not None:
            self.catalog_item = catalog_item
        if technical_system_list is not None:
            self.technical_system_list = technical_system_list
        if catalog_item_id is not None:
            self.catalog_item_id = catalog_item_id
        if catalog_item_string is not None:
            self.catalog_item_string = catalog_item_string

    @property
    def alternate_name(self):
        """Gets the alternate_name of this ItemDomainCableDesignAllOf.  # noqa: E501


        :return: The alternate_name of this ItemDomainCableDesignAllOf.  # noqa: E501
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this ItemDomainCableDesignAllOf.


        :param alternate_name: The alternate_name of this ItemDomainCableDesignAllOf.  # noqa: E501
        :type: str
        """

        self._alternate_name = alternate_name

    @property
    def catalog_item(self):
        """Gets the catalog_item of this ItemDomainCableDesignAllOf.  # noqa: E501


        :return: The catalog_item of this ItemDomainCableDesignAllOf.  # noqa: E501
        :rtype: Item
        """
        return self._catalog_item

    @catalog_item.setter
    def catalog_item(self, catalog_item):
        """Sets the catalog_item of this ItemDomainCableDesignAllOf.


        :param catalog_item: The catalog_item of this ItemDomainCableDesignAllOf.  # noqa: E501
        :type: Item
        """

        self._catalog_item = catalog_item

    @property
    def technical_system_list(self):
        """Gets the technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501


        :return: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
        :rtype: list[ItemCategory]
        """
        return self._technical_system_list

    @technical_system_list.setter
    def technical_system_list(self, technical_system_list):
        """Sets the technical_system_list of this ItemDomainCableDesignAllOf.


        :param technical_system_list: The technical_system_list of this ItemDomainCableDesignAllOf.  # noqa: E501
        :type: list[ItemCategory]
        """

        self._technical_system_list = technical_system_list

    @property
    def catalog_item_id(self):
        """Gets the catalog_item_id of this ItemDomainCableDesignAllOf.  # noqa: E501


        :return: The catalog_item_id of this ItemDomainCableDesignAllOf.  # noqa: E501
        :rtype: str
        """
        return self._catalog_item_id

    @catalog_item_id.setter
    def catalog_item_id(self, catalog_item_id):
        """Sets the catalog_item_id of this ItemDomainCableDesignAllOf.


        :param catalog_item_id: The catalog_item_id of this ItemDomainCableDesignAllOf.  # noqa: E501
        :type: str
        """

        self._catalog_item_id = catalog_item_id

    @property
    def catalog_item_string(self):
        """Gets the catalog_item_string of this ItemDomainCableDesignAllOf.  # noqa: E501


        :return: The catalog_item_string of this ItemDomainCableDesignAllOf.  # noqa: E501
        :rtype: str
        """
        return self._catalog_item_string

    @catalog_item_string.setter
    def catalog_item_string(self, catalog_item_string):
        """Sets the catalog_item_string of this ItemDomainCableDesignAllOf.


        :param catalog_item_string: The catalog_item_string of this ItemDomainCableDesignAllOf.  # noqa: E501
        :type: str
        """

        self._catalog_item_string = catalog_item_string

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
        if not isinstance(other, ItemDomainCableDesignAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemDomainCableDesignAllOf):
            return True

        return self.to_dict() != other.to_dict()
