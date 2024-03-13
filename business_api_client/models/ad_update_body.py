# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class AdUpdateBody(object):
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
        'adgroup_id': 'str',
        'advertiser_id': 'str',
        'creatives': 'list[OpenApiv13adupdateCreatives]'
    }

    attribute_map = {
        'adgroup_id': 'adgroup_id',
        'advertiser_id': 'advertiser_id',
        'creatives': 'creatives'
    }

    def __init__(self, adgroup_id=None, advertiser_id=None, creatives=None):  # noqa: E501
        """AdUpdateBody - a model defined in Swagger"""  # noqa: E501
        self._adgroup_id = None
        self._advertiser_id = None
        self._creatives = None
        self.discriminator = None
        self.adgroup_id = adgroup_id
        self.advertiser_id = advertiser_id
        self.creatives = creatives

    @property
    def adgroup_id(self):
        """Gets the adgroup_id of this AdUpdateBody.  # noqa: E501

        Ad group ID  # noqa: E501

        :return: The adgroup_id of this AdUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._adgroup_id

    @adgroup_id.setter
    def adgroup_id(self, adgroup_id):
        """Sets the adgroup_id of this AdUpdateBody.

        Ad group ID  # noqa: E501

        :param adgroup_id: The adgroup_id of this AdUpdateBody.  # noqa: E501
        :type: str
        """
        if adgroup_id is None:
            raise ValueError("Invalid value for `adgroup_id`, must not be `None`")  # noqa: E501

        self._adgroup_id = adgroup_id

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this AdUpdateBody.  # noqa: E501

        Advertiser ID  # noqa: E501

        :return: The advertiser_id of this AdUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this AdUpdateBody.

        Advertiser ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this AdUpdateBody.  # noqa: E501
        :type: str
        """
        if advertiser_id is None:
            raise ValueError("Invalid value for `advertiser_id`, must not be `None`")  # noqa: E501

        self._advertiser_id = advertiser_id

    @property
    def creatives(self):
        """Gets the creatives of this AdUpdateBody.  # noqa: E501

        Advertising creatives.  # noqa: E501

        :return: The creatives of this AdUpdateBody.  # noqa: E501
        :rtype: list[OpenApiv13adupdateCreatives]
        """
        return self._creatives

    @creatives.setter
    def creatives(self, creatives):
        """Sets the creatives of this AdUpdateBody.

        Advertising creatives.  # noqa: E501

        :param creatives: The creatives of this AdUpdateBody.  # noqa: E501
        :type: list[OpenApiv13adupdateCreatives]
        """
        if creatives is None:
            raise ValueError("Invalid value for `creatives`, must not be `None`")  # noqa: E501

        self._creatives = creatives

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
        if issubclass(AdUpdateBody, dict):
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
        if not isinstance(other, AdUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other