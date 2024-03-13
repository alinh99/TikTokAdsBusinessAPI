# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class CampaignUpdateBody(object):
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
        'advertiser_id': 'str',
        'budget': 'float',
        'budget_mode': 'str',
        'campaign_id': 'str',
        'campaign_name': 'str',
        'roas_bid': 'float',
        'special_industries': 'list[str]'
    }

    attribute_map = {
        'advertiser_id': 'advertiser_id',
        'budget': 'budget',
        'budget_mode': 'budget_mode',
        'campaign_id': 'campaign_id',
        'campaign_name': 'campaign_name',
        'roas_bid': 'roas_bid',
        'special_industries': 'special_industries'
    }

    def __init__(self, advertiser_id=None, budget=None, budget_mode=None, campaign_id=None, campaign_name=None, roas_bid=None, special_industries=None):  # noqa: E501
        """CampaignUpdateBody - a model defined in Swagger"""  # noqa: E501
        self._advertiser_id = None
        self._budget = None
        self._budget_mode = None
        self._campaign_id = None
        self._campaign_name = None
        self._roas_bid = None
        self._special_industries = None
        self.discriminator = None
        self.advertiser_id = advertiser_id
        if budget is not None:
            self.budget = budget
        if budget_mode is not None:
            self.budget_mode = budget_mode
        self.campaign_id = campaign_id
        if campaign_name is not None:
            self.campaign_name = campaign_name
        if roas_bid is not None:
            self.roas_bid = roas_bid
        if special_industries is not None:
            self.special_industries = special_industries

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this CampaignUpdateBody.  # noqa: E501

        Advertiser ID  # noqa: E501

        :return: The advertiser_id of this CampaignUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this CampaignUpdateBody.

        Advertiser ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this CampaignUpdateBody.  # noqa: E501
        :type: str
        """
        if advertiser_id is None:
            raise ValueError("Invalid value for `advertiser_id`, must not be `None`")  # noqa: E501

        self._advertiser_id = advertiser_id

    @property
    def budget(self):
        """Gets the budget of this CampaignUpdateBody.  # noqa: E501

        Campaign budget. Required when budget_mode is BUDGET_MODE_DAY or BUDGET_MODE_TOTAL. To learn about the mininum budget and how to set budget types, see Budget settings.  # noqa: E501

        :return: The budget of this CampaignUpdateBody.  # noqa: E501
        :rtype: float
        """
        return self._budget

    @budget.setter
    def budget(self, budget):
        """Sets the budget of this CampaignUpdateBody.

        Campaign budget. Required when budget_mode is BUDGET_MODE_DAY or BUDGET_MODE_TOTAL. To learn about the mininum budget and how to set budget types, see Budget settings.  # noqa: E501

        :param budget: The budget of this CampaignUpdateBody.  # noqa: E501
        :type: float
        """

        self._budget = budget

    @property
    def budget_mode(self):
        """Gets the budget_mode of this CampaignUpdateBody.  # noqa: E501

        Budget type. When Campaign Budgeet Optimization is enabled, only BUDGET_MODE_DAY is supported. To learn about how to set budget types, see Budget setting.  # noqa: E501

        :return: The budget_mode of this CampaignUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._budget_mode

    @budget_mode.setter
    def budget_mode(self, budget_mode):
        """Sets the budget_mode of this CampaignUpdateBody.

        Budget type. When Campaign Budgeet Optimization is enabled, only BUDGET_MODE_DAY is supported. To learn about how to set budget types, see Budget setting.  # noqa: E501

        :param budget_mode: The budget_mode of this CampaignUpdateBody.  # noqa: E501
        :type: str
        """

        self._budget_mode = budget_mode

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignUpdateBody.  # noqa: E501

        Campaign name. It can contain up to 512 characters. Emoji is not supported. Note: Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.  # noqa: E501

        :return: The campaign_id of this CampaignUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignUpdateBody.

        Campaign name. It can contain up to 512 characters. Emoji is not supported. Note: Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.  # noqa: E501

        :param campaign_id: The campaign_id of this CampaignUpdateBody.  # noqa: E501
        :type: str
        """
        if campaign_id is None:
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this CampaignUpdateBody.  # noqa: E501

        Campaign name. It can contain up to 512 characters. Emoji is not supported. Note: Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.  # noqa: E501

        :return: The campaign_name of this CampaignUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this CampaignUpdateBody.

        Campaign name. It can contain up to 512 characters. Emoji is not supported. Note: Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.  # noqa: E501

        :param campaign_name: The campaign_name of this CampaignUpdateBody.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def roas_bid(self):
        """Gets the roas_bid of this CampaignUpdateBody.  # noqa: E501

        ROAS (Return On Advertising Spend) goal to optimize value. This field can be modified only when Campaign Budget Optimization(budget_optimize_on) is enabled , optimization_goal is VALUE and deep_bid_type is VO_MIN_ROAS. Value range: 0.01-1000.  # noqa: E501

        :return: The roas_bid of this CampaignUpdateBody.  # noqa: E501
        :rtype: float
        """
        return self._roas_bid

    @roas_bid.setter
    def roas_bid(self, roas_bid):
        """Sets the roas_bid of this CampaignUpdateBody.

        ROAS (Return On Advertising Spend) goal to optimize value. This field can be modified only when Campaign Budget Optimization(budget_optimize_on) is enabled , optimization_goal is VALUE and deep_bid_type is VO_MIN_ROAS. Value range: 0.01-1000.  # noqa: E501

        :param roas_bid: The roas_bid of this CampaignUpdateBody.  # noqa: E501
        :type: float
        """

        self._roas_bid = roas_bid

    @property
    def special_industries(self):
        """Gets the special_industries of this CampaignUpdateBody.  # noqa: E501

        Ad categories. Enum values: HOUSING(Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities.) EMPLOYMENT(Ads for job offers, internship, professional certification programs or other related opportunities.) CREDIT(Ads for credit card offers, auto loans, long-term financing or other related opportunities.) Note: The ONLY supported operation here is that you can clear all the values for the field if you've specifed it when creating a campaign. If you've not specified the field when creating a campaign, you cannot specify it now either.  # noqa: E501

        :return: The special_industries of this CampaignUpdateBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._special_industries

    @special_industries.setter
    def special_industries(self, special_industries):
        """Sets the special_industries of this CampaignUpdateBody.

        Ad categories. Enum values: HOUSING(Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities.) EMPLOYMENT(Ads for job offers, internship, professional certification programs or other related opportunities.) CREDIT(Ads for credit card offers, auto loans, long-term financing or other related opportunities.) Note: The ONLY supported operation here is that you can clear all the values for the field if you've specifed it when creating a campaign. If you've not specified the field when creating a campaign, you cannot specify it now either.  # noqa: E501

        :param special_industries: The special_industries of this CampaignUpdateBody.  # noqa: E501
        :type: list[str]
        """

        self._special_industries = special_industries

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
        if issubclass(CampaignUpdateBody, dict):
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
        if not isinstance(other, CampaignUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other