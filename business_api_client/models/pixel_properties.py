# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class PixelProperties(object):
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
        'contents': 'list[PixelContent]',
        'currency': 'str',
        'description': 'str',
        'query': 'str',
        'value': 'float'
    }

    attribute_map = {
        'contents': 'contents',
        'currency': 'currency',
        'description': 'description',
        'query': 'query',
        'value': 'value'
    }

    def __init__(self, contents=None, currency=None, description=None, query=None, value=None):  # noqa: E501
        """PixelProperties - a model defined in Swagger"""  # noqa: E501
        self._contents = None
        self._currency = None
        self._description = None
        self._query = None
        self._value = None
        self.discriminator = None
        if contents is not None:
            self.contents = contents
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if query is not None:
            self.query = query
        if value is not None:
            self.value = value

    @property
    def contents(self):
        """Gets the contents of this PixelProperties.  # noqa: E501

        Related items in a web event (e.g. items added in an Initiate Checkout event).  # noqa: E501

        :return: The contents of this PixelProperties.  # noqa: E501
        :rtype: list[PixelContent]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this PixelProperties.

        Related items in a web event (e.g. items added in an Initiate Checkout event).  # noqa: E501

        :param contents: The contents of this PixelProperties.  # noqa: E501
        :type: list[PixelContent]
        """

        self._contents = contents

    @property
    def currency(self):
        """Gets the currency of this PixelProperties.  # noqa: E501

        ISO 4217 code. Examples: EUR, USD, JPY. List of currencies currently supported: AED, ARS, AUD, BDT, BHD, BIF, BOB, BRL, CAD, CHF, CLP, CNY, COP, CRC, CZK, DKK, DZD, EGP, EUR, GBP, GTQ, HKD, HNL, HUF, IDR, ILS, INR, ISK, JPY, KES, KHR, KRW, KWD, KZT, MAD, MOP, MXN, MYR, NGN, NIO, NOK, NZD, OMR, PEN, PHP, PHP, PKR, PLN, PYG, QAR, RON, RUB, SAR, SEK, SGD, THB, TRY, TWD, UAH, USD, VES, VND, ZAR.  # noqa: E501

        :return: The currency of this PixelProperties.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PixelProperties.

        ISO 4217 code. Examples: EUR, USD, JPY. List of currencies currently supported: AED, ARS, AUD, BDT, BHD, BIF, BOB, BRL, CAD, CHF, CLP, CNY, COP, CRC, CZK, DKK, DZD, EGP, EUR, GBP, GTQ, HKD, HNL, HUF, IDR, ILS, INR, ISK, JPY, KES, KHR, KRW, KWD, KZT, MAD, MOP, MXN, MYR, NGN, NIO, NOK, NZD, OMR, PEN, PHP, PHP, PKR, PLN, PYG, QAR, RON, RUB, SAR, SEK, SGD, THB, TRY, TWD, UAH, USD, VES, VND, ZAR.  # noqa: E501

        :param currency: The currency of this PixelProperties.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this PixelProperties.  # noqa: E501

        Description of the item or page.  # noqa: E501

        :return: The description of this PixelProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PixelProperties.

        Description of the item or page.  # noqa: E501

        :param description: The description of this PixelProperties.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def query(self):
        """Gets the query of this PixelProperties.  # noqa: E501

        The text string that was input by a user. For instance, if a person searches for a product on your website, you can forward the keyword being searched. If a person enters a coupon code at check out, you can forward the code.  # noqa: E501

        :return: The query of this PixelProperties.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PixelProperties.

        The text string that was input by a user. For instance, if a person searches for a product on your website, you can forward the keyword being searched. If a person enters a coupon code at check out, you can forward the code.  # noqa: E501

        :param query: The query of this PixelProperties.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def value(self):
        """Gets the value of this PixelProperties.  # noqa: E501

        Value of the order or items sold. Note: Price is the price for a single item, and value is the total price of the order. For example, if you have two items each sold for $10, the price parameter would pass 10 and the value parameter would pass 20.  # noqa: E501

        :return: The value of this PixelProperties.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PixelProperties.

        Value of the order or items sold. Note: Price is the price for a single item, and value is the total price of the order. For example, if you have two items each sold for $10, the price parameter would pass 10 and the value parameter would pass 20.  # noqa: E501

        :param value: The value of this PixelProperties.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(PixelProperties, dict):
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
        if not isinstance(other, PixelProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
