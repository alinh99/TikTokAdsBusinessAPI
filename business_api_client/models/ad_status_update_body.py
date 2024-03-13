# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class AdStatusUpdateBody(object):
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
        'aco_ad_ids': 'list[str]',
        'ad_ids': 'list[str]',
        'advertiser_id': 'str',
        'operation_status': 'str'
    }

    attribute_map = {
        'aco_ad_ids': 'aco_ad_ids',
        'ad_ids': 'ad_ids',
        'advertiser_id': 'advertiser_id',
        'operation_status': 'operation_status'
    }

    def __init__(self, aco_ad_ids=None, ad_ids=None, advertiser_id=None, operation_status=None):  # noqa: E501
        """AdStatusUpdateBody - a model defined in Swagger"""  # noqa: E501
        self._aco_ad_ids = None
        self._ad_ids = None
        self._advertiser_id = None
        self._operation_status = None
        self.discriminator = None
        if aco_ad_ids is not None:
            self.aco_ad_ids = aco_ad_ids
        if ad_ids is not None:
            self.ad_ids = ad_ids
        self.advertiser_id = advertiser_id
        self.operation_status = operation_status

    @property
    def aco_ad_ids(self):
        """Gets the aco_ad_ids of this AdStatusUpdateBody.  # noqa: E501

        A list of ACO ad IDs. Only support `ENABLE` and `DISABLE` for ACO ads.  Allowed quantity- `1-20`. Either `ad_ids` or `aco_ad_ids` has to be set.  # noqa: E501

        :return: The aco_ad_ids of this AdStatusUpdateBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._aco_ad_ids

    @aco_ad_ids.setter
    def aco_ad_ids(self, aco_ad_ids):
        """Sets the aco_ad_ids of this AdStatusUpdateBody.

        A list of ACO ad IDs. Only support `ENABLE` and `DISABLE` for ACO ads.  Allowed quantity- `1-20`. Either `ad_ids` or `aco_ad_ids` has to be set.  # noqa: E501

        :param aco_ad_ids: The aco_ad_ids of this AdStatusUpdateBody.  # noqa: E501
        :type: list[str]
        """

        self._aco_ad_ids = aco_ad_ids

    @property
    def ad_ids(self):
        """Gets the ad_ids of this AdStatusUpdateBody.  # noqa: E501

        A list of ad IDs. Allowed quantity- `1-20`. Either `ad_ids` or `aco_ad_ids` has to be set.  # noqa: E501

        :return: The ad_ids of this AdStatusUpdateBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._ad_ids

    @ad_ids.setter
    def ad_ids(self, ad_ids):
        """Sets the ad_ids of this AdStatusUpdateBody.

        A list of ad IDs. Allowed quantity- `1-20`. Either `ad_ids` or `aco_ad_ids` has to be set.  # noqa: E501

        :param ad_ids: The ad_ids of this AdStatusUpdateBody.  # noqa: E501
        :type: list[str]
        """

        self._ad_ids = ad_ids

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this AdStatusUpdateBody.  # noqa: E501

        Advertiser ID  # noqa: E501

        :return: The advertiser_id of this AdStatusUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this AdStatusUpdateBody.

        Advertiser ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this AdStatusUpdateBody.  # noqa: E501
        :type: str
        """
        if advertiser_id is None:
            raise ValueError("Invalid value for `advertiser_id`, must not be `None`")  # noqa: E501

        self._advertiser_id = advertiser_id

    @property
    def operation_status(self):
        """Gets the operation_status of this AdStatusUpdateBody.  # noqa: E501

        The operation being made. Enum values- `DELETE` (delete),` DISABLE` (pause), `ENABLE` (enable).  The status of deleted ads cannot be modified.  # noqa: E501

        :return: The operation_status of this AdStatusUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """Sets the operation_status of this AdStatusUpdateBody.

        The operation being made. Enum values- `DELETE` (delete),` DISABLE` (pause), `ENABLE` (enable).  The status of deleted ads cannot be modified.  # noqa: E501

        :param operation_status: The operation_status of this AdStatusUpdateBody.  # noqa: E501
        :type: str
        """
        if operation_status is None:
            raise ValueError("Invalid value for `operation_status`, must not be `None`")  # noqa: E501

        self._operation_status = operation_status

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
        if issubclass(AdStatusUpdateBody, dict):
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
        if not isinstance(other, AdStatusUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
