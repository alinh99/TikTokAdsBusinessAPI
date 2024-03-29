# TikTok Business API SDK - Python

Comprehensive collection of client libraries that enable our developers to build software to integrate with Business API faster and in a more standardized way.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.1

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

Please refer to the "Integration with Python SDK" section in the [README.md](https://github.com/tiktok/tiktok-business-api-sdk/blob/main/README.md) under the root folder.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import business_api_client
from business_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = business_api_client.AccountApi(business_api_client.ApiClient(configuration))
access_token = 'access_token_example' # str | Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162).
body = business_api_client.AdvertiserUpdateBody() # AdvertiserUpdateBody | Advertiser update body parameters (optional)

try:
    # Update an ad account [Advertiser Update](https://ads.tiktok.com/marketing_api/docs?id=1739939050770434)
    api_response = api_instance.advertiser_update(access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->advertiser_update: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://business-api.tiktok.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**advertiser_update**](docs/AccountApi.md#advertiser_update) | **POST** /open_api/v1.3/advertiser/update/ | Update an ad account [Advertiser Update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939050770434)
*AdApi* | [**ad_create**](docs/AdApi.md#ad_create) | **POST** /open_api/v1.3/ad/create/ | Upload your ad creatives (pictures, videos, texts, call-to-action) and create an ad. For different placements, the creative formats and requirements are different. Upload your ad creatives according to the placement requirements. Each ad group can have up to 20 ads. See here to learn about how to create ads. [Ad create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739953377508354)
*AdApi* | [**ad_get**](docs/AdApi.md#ad_get) | **GET** /open_api/v1.3/ad/get/ | Get the data of regular ads and ACO ads. [Ad get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1735735588640770)
*AdApi* | [**ad_status_update**](docs/AdApi.md#ad_status_update) | **POST** /open_api/v1.3/ad/status/update/ | To enable, disable or delete an ad or ads [Ad status update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739953422970882)
*AdApi* | [**ad_update**](docs/AdApi.md#ad_update) | **POST** /open_api/v1.3/ad/update/ | Modify your custom ad creatives such as call-to-action, ad name, text image and video material. To update ACO ads, use the /ad/aco/update/ endpoint. [Ad update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739953422970882)
*AdAcoApi* | [**ad_aco_create**](docs/AdAcoApi.md#ad_aco_create) | **POST** /open_api/v1.3/ad/aco/create/ | Create an ACO ad by uploading necessary ad creatives to the library. [Ad Aco Create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739473063234626)
*AdAcoApi* | [**ad_aco_get**](docs/AdAcoApi.md#ad_aco_get) | **GET** /open_api/v1.3/ad/aco/get/ | Get creative materials for an ACO ad, including call-to-actions, texts, ad names, images, or video materials. [Ad Aco Get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739473020978177)
*AdAcoApi* | [**ad_aco_material_status_update**](docs/AdAcoApi.md#ad_aco_material_status_update) | **POST** /open_api/v1.3/ad/aco/material_status/update/ | Update the status of creative materials for an ACO ad, including ad texts, images, and video materials [Update materials](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739506701165570)
*AdAcoApi* | [**ad_aco_update**](docs/AdAcoApi.md#ad_aco_update) | **POST** /open_api/v1.3/ad/aco/update/ | Modify ACO ad creatives. [Update ACO](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739473077112833)
*AdgroupApi* | [**adgroup_create**](docs/AdgroupApi.md#adgroup_create) | **POST** /open_api/v1.3/adgroup/create/ | Create an ad group. At the ad group level, you can configure placement, audience settings (see Ad Targeting), budget, schedules, as well as bidding and optimization options for ads. To learn about the procedure and the essential data fields to create an ad group, see Create an Ad Group. [Ad Update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739499616346114)
*AdgroupApi* | [**adgroup_get**](docs/AdgroupApi.md#adgroup_get) | **GET** /open_api/v1.3/adgroup/get/ | Obtain detailed information of an ad group or ad groups. [Adgroup get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739314558673922)
*AdgroupApi* | [**adgroup_status_update**](docs/AdgroupApi.md#adgroup_status_update) | **POST** /open_api/v1.3/adgroup/status/update/ | Enable, disable or delete an ad group. [Adgroup status update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739591716326402)
*AdgroupApi* | [**adgroup_update**](docs/AdgroupApi.md#adgroup_update) | **POST** /open_api/v1.3/adgroup/update/ | Obtain detailed information of an ad group or ad groups. [Adgroup update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739586761631745)
*AudienceApi* | [**dmp_custom_audience_list**](docs/AudienceApi.md#dmp_custom_audience_list) | **GET** /open_api/v1.3/dmp/custom_audience/list/ | Get all audiences [DMP cusom audience list](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739940506015746)
*AuthenticationApi* | [**oauth2_access_token**](docs/AuthenticationApi.md#oauth2_access_token) | **POST** /open_api/v1.3/oauth2/access_token/ | Get access_token and refresh_token by auth_code. The creator access token is valid for 24 hours and the refresh token is valid for one year. Within one year you will need to refresh the access token with the refresh token on a daily basis. After one year you will need to ask the creator to reauthorize. [Oauth2 Access Token](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739965703387137)
*AuthenticationApi* | [**oauth2_advertiser_get**](docs/AuthenticationApi.md#oauth2_advertiser_get) | **GET** /open_api/v1.3/oauth2/advertiser/get/ | Obtain a list of advertiser accounts that authorized an app. [Advertiser Get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1738455508553729)
*BCApi* | [**bc_advertiser_create**](docs/BCApi.md#bc_advertiser_create) | **POST** /open_api/v1.3/bc/advertiser/create/ | Create an ad account [BC advertiser create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939020318721)
*BCApi* | [**bc_asset_get**](docs/BCApi.md#bc_asset_get) | **GET** /open_api/v1.3/bc/asset/get/ | Get assets [BC asset get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739432717798401)
*BCApi* | [**bc_get**](docs/BCApi.md#bc_get) | **GET** /open_api/v1.3/bc/get/ | Get Business Centers [BC get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737115687501826)
*BCApi* | [**bc_image_upload**](docs/BCApi.md#bc_image_upload) | **POST** /open_api/v1.3/bc/image/upload/ | Upload a business certificate [BC image upload](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739938996913218)
*BcPaymentApi* | [**advertiser_balance_get**](docs/BcPaymentApi.md#advertiser_balance_get) | **GET** /open_api/v1.3/advertiser/balance/get/ | Obtain the balance of ad accounts in the Business Center. This function only returns the ad accounts that the Business Center has administrator permissions over. [Advertiser balance get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939106470913)
*BcPaymentApi* | [**advertiser_transaction_get**](docs/BcPaymentApi.md#advertiser_transaction_get) | **GET** /open_api/v1.3/advertiser/transaction/get/ | Get the transaction records of ad accounts in the Business Center. This function only returns the transaction records of ad accounts that the Business Center has administrator rights over. [Advertiser transaction Get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939116353538)
*BcPaymentApi* | [**bc_balance_get**](docs/BcPaymentApi.md#bc_balance_get) | **GET** /open_api/v1.3/bc/balance/get/ | Obtain the balance of a Business Center. [Balance get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939128198145)
*BcPaymentApi* | [**bc_transaction_get**](docs/BcPaymentApi.md#bc_transaction_get) | **GET** /open_api/v1.3/bc/transaction/get/ | Get the transaction records of your Business Centers. [Transaction get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939140408322)
*BcPaymentApi* | [**bc_transfer**](docs/BcPaymentApi.md#bc_transfer) | **POST** /open_api/v1.3/bc/transfer/ | Recharge money to or deduct money from an ad account in a Business Center. [BC transfer](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739939095321601)
*CampaignCreationApi* | [**campaign_create**](docs/CampaignCreationApi.md#campaign_create) | **POST** /open_api/v1.3/campaign/create/ | To create a campaign. To advertise on TikTok Ads, you need to create a campaign and set the Advertising objectives and budget. A regular campaign can contain one or more ad groups. [Campaign Create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739318962329602)
*CampaignCreationApi* | [**campaign_get**](docs/CampaignCreationApi.md#campaign_get) | **GET** /open_api/v1.3/campaign/get/ | Get all campaigns for an ad account. Optionally, you can use filters in your request to return only certain campaigns. [Campaign get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739315828649986)
*CampaignCreationApi* | [**campaign_status_update**](docs/CampaignCreationApi.md#campaign_status_update) | **POST** /open_api/v1.3/campaign/status/update/ | Enable, disable or delete a campaign. [Campaign status update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739320994354178)
*CampaignCreationApi* | [**campaign_update**](docs/CampaignCreationApi.md#campaign_update) | **POST** /open_api/v1.3/campaign/update/ | To modify a campaign after it has been created. Information like campaign name, budget, and budget type can be updated. [Campaign Update](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739320422086657)
*CreativeAssetApi* | [**creative_portfolio_create**](docs/CreativeAssetApi.md#creative_portfolio_create) | **POST** /open_api/v1.3/creative/portfolio/create/ | Create a portfolio [Portfolio create](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739091950439426)
*EventCallbackApi* | [**pixel_batch**](docs/EventCallbackApi.md#pixel_batch) | **POST** /open_api/v1.3/pixel/batch/ | Pixel Track server-to-server batch api
*EventCallbackApi* | [**pixel_track**](docs/EventCallbackApi.md#pixel_track) | **POST** /open_api/v1.3/pixel/track/ | Pixel Track server-to-server api
*FileApi* | [**ad_image_info**](docs/FileApi.md#ad_image_info) | **GET** /open_api/v1.3/file/image/ad/info/ | The function is used to obtain the information of images from the Asset Library. [File image info](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1740051721711618)
*FileApi* | [**ad_image_upload**](docs/FileApi.md#ad_image_upload) | **POST** /open_api/v1.3/file/image/ad/upload/ | The function is used to  to upload pictures to the Asset Library and use the obtained image ID for creating ads. [File image Upload](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1739067433456642)
*FileApi* | [**ad_video_info**](docs/FileApi.md#ad_video_info) | **GET** /open_api/v1.3/file/video/ad/info/ | The function is used to get the information about a list of videos [File Video Ad Info](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1740050161973250) from the Asset Library.
*FileApi* | [**ad_video_search**](docs/FileApi.md#ad_video_search) | **GET** /open_api/v1.3/file/video/ad/search/ | The function is used to to search for video creatives in the Asset Library of an ad account. [File Video Search](to search for video creatives in the Asset Library of an ad account.) Library.
*FileApi* | [**ad_video_upload**](docs/FileApi.md#ad_video_upload) | **POST** /open_api/v1.3/file/video/ad/upload/ | The function is used to upload a video to the Asset Library and use the obtained video ID for creating ads. [File Video Upload](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737587322856449)
*IdentityApi* | [**identity_create**](docs/IdentityApi.md#identity_create) | **POST** /open_api/v1.3/identity/create/ | Create a customized user identity. [Identity Create](https://ads.tiktok.com/marketing_api/docs?rid&#x3D;uraumvplog&amp;id&#x3D;1740654203526146)
*IdentityApi* | [**identity_get**](docs/IdentityApi.md#identity_get) | **GET** /open_api/v1.3/identity/get/ | Get a list of identities under an ad account. You can filter results by identity type. [Identity Get](https://ads.tiktok.com/marketing_api/docs?rid&#x3D;uraumvplog&amp;id&#x3D;1740218420781057)
*IdentityApi* | [**identity_video_info**](docs/IdentityApi.md#identity_video_info) | **GET** /open_api/v1.3/identity/video/info/ | Get the information about a TikTok post that you own, if your identity is AUTH_CODE, TT_USER or BC_AUTH_TT. [Identity Video Info](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1738958351620097)
*MeasurementApi* | [**app_list**](docs/MeasurementApi.md#app_list) | **GET** /open_api/v1.3/app/list/ | Get the app list [App list](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1740859313270786)
*MeasurementApi* | [**app_optimization_event**](docs/MeasurementApi.md#app_optimization_event) | **GET** /open_api/v1.3/app/optimization_event/ | Get App Events [App events](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1740859338750977)
*RecommendToolApi* | [**tool_targeting_category_recommend**](docs/RecommendToolApi.md#tool_targeting_category_recommend) | **POST** /open_api/v1.3/tool/targeting_category/recommend/ | Get recommended interest and action categories [Tool targeting category](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1736275204260866)
*ReportingApi* | [**report_integrated_get**](docs/ReportingApi.md#report_integrated_get) | **GET** /open_api/v1.3/report/integrated/get/ | Create a synchronous report task.  This endpoint can currently return the reporting data of up to 10,000 advertisements. If your number of advertisements exceeds 10,000, please use campaign_ids / adgroup_ids / ad_ids as a filter to obtain the reporting data of all advertisements in batches. Additionally, with CHUNK mode on, up to 20,000 advertisements can be returned. If you use campaign_ids / adgroup_ids / ad_ids as a filter, you can pass in up to 100 IDs at a time. [Reporting Get](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1740302848100353)
*ToolApi* | [**tool_action_category**](docs/ToolApi.md#tool_action_category) | **GET** /open_api/v1.3/tool/action_category/ | Get action categories [Tool action](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737166752522241)
*ToolApi* | [**tool_carrier**](docs/ToolApi.md#tool_carrier) | **GET** /open_api/v1.3/tool/carrier/ | Get carriers [Tool carrier](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737168013095938)
*ToolApi* | [**tool_device_model**](docs/ToolApi.md#tool_device_model) | **GET** /open_api/v1.3/tool/device_model/ | Get device models [Tool device model](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737172880570369)
*ToolApi* | [**tool_interest_category**](docs/ToolApi.md#tool_interest_category) | **GET** /open_api/v1.3/tool/interest_category/ | Get interest categories [Tool Interest category](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737174348712961)
*ToolApi* | [**tool_interest_keyword_recommend**](docs/ToolApi.md#tool_interest_keyword_recommend) | **GET** /open_api/v1.3/tool/interest_keyword/recommend/ | Get interest keywords [Tool kyword recommend](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737180852720642)
*ToolApi* | [**tool_language**](docs/ToolApi.md#tool_language) | **GET** /open_api/v1.3/tool/language/ | Get languages [Tool Language](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737188554152962)
*ToolApi* | [**tool_region**](docs/ToolApi.md#tool_region) | **GET** /open_api/v1.3/tool/region/ | Get available locations [Tool Region](https://ads.tiktok.com/marketing_api/docs?id&#x3D;1737189539571713)

## Documentation For Models

 - [AdAcoBody](docs/AdAcoBody.md)
 - [AdAcoBodyAvatarIcon](docs/AdAcoBodyAvatarIcon.md)
 - [AdAcoBodyAvatarIconList](docs/AdAcoBodyAvatarIconList.md)
 - [AdAcoBodyCallToActionList](docs/AdAcoBodyCallToActionList.md)
 - [AdAcoBodyCardList](docs/AdAcoBodyCardList.md)
 - [AdAcoBodyCommonMaterial](docs/AdAcoBodyCommonMaterial.md)
 - [AdAcoBodyCommonMaterialTrackingInfo](docs/AdAcoBodyCommonMaterialTrackingInfo.md)
 - [AdAcoBodyDeeplinkList](docs/AdAcoBodyDeeplinkList.md)
 - [AdAcoBodyDisplayNameList](docs/AdAcoBodyDisplayNameList.md)
 - [AdAcoBodyLandingPageUrls](docs/AdAcoBodyLandingPageUrls.md)
 - [AdAcoBodyMediaInfo](docs/AdAcoBodyMediaInfo.md)
 - [AdAcoBodyMediaInfoImageInfo](docs/AdAcoBodyMediaInfoImageInfo.md)
 - [AdAcoBodyMediaInfoList](docs/AdAcoBodyMediaInfoList.md)
 - [AdAcoBodyMediaInfoVideoInfo](docs/AdAcoBodyMediaInfoVideoInfo.md)
 - [AdAcoBodyPageList](docs/AdAcoBodyPageList.md)
 - [AdAcoBodyTitleList](docs/AdAcoBodyTitleList.md)
 - [AdAcoUpdateBody](docs/AdAcoUpdateBody.md)
 - [AdCreateBody](docs/AdCreateBody.md)
 - [AdStatusUpdateBody](docs/AdStatusUpdateBody.md)
 - [AdUpdateBody](docs/AdUpdateBody.md)
 - [AdUploadBody](docs/AdUploadBody.md)
 - [AdgroupCreateBody](docs/AdgroupCreateBody.md)
 - [AdgroupStatusUpdateBody](docs/AdgroupStatusUpdateBody.md)
 - [AdgroupUpdateBody](docs/AdgroupUpdateBody.md)
 - [AdvertiserCreateBody](docs/AdvertiserCreateBody.md)
 - [AdvertiserUpdateBody](docs/AdvertiserUpdateBody.md)
 - [BcTransferBody](docs/BcTransferBody.md)
 - [CampaignCreateBody](docs/CampaignCreateBody.md)
 - [CampaignStatusUpdateBody](docs/CampaignStatusUpdateBody.md)
 - [CampaignUpdateBody](docs/CampaignUpdateBody.md)
 - [FileImageAdUpload](docs/FileImageAdUpload.md)
 - [Filtering](docs/Filtering.md)
 - [FilteringAdGet](docs/FilteringAdGet.md)
 - [FilteringAdgroupGet](docs/FilteringAdgroupGet.md)
 - [FilteringAdvertiserBalanceGet](docs/FilteringAdvertiserBalanceGet.md)
 - [FilteringAdvertiserTransactionGet](docs/FilteringAdvertiserTransactionGet.md)
 - [FilteringBCTransactionGet](docs/FilteringBCTransactionGet.md)
 - [FilteringCampaignGet](docs/FilteringCampaignGet.md)
 - [FilteringReportIntegratedGet](docs/FilteringReportIntegratedGet.md)
 - [FilteringVideoAdSearch](docs/FilteringVideoAdSearch.md)
 - [IdentityCreateBody](docs/IdentityCreateBody.md)
 - [ImageUploadBody](docs/ImageUploadBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [MaterialStatusUpdateBody](docs/MaterialStatusUpdateBody.md)
 - [Oauth2AccessTokenBody](docs/Oauth2AccessTokenBody.md)
 - [OpenApiv13adcreateCreatives](docs/OpenApiv13adcreateCreatives.md)
 - [OpenApiv13adcreateDisclaimerClickableTexts](docs/OpenApiv13adcreateDisclaimerClickableTexts.md)
 - [OpenApiv13adcreateDisclaimerText](docs/OpenApiv13adcreateDisclaimerText.md)
 - [OpenApiv13adgroupcreateActions](docs/OpenApiv13adgroupcreateActions.md)
 - [OpenApiv13adgroupcreateAudienceRule](docs/OpenApiv13adgroupcreateAudienceRule.md)
 - [OpenApiv13adgroupcreateAudienceRuleExclusions](docs/OpenApiv13adgroupcreateAudienceRuleExclusions.md)
 - [OpenApiv13adgroupcreateAudienceRuleExclusionsEventSources](docs/OpenApiv13adgroupcreateAudienceRuleExclusionsEventSources.md)
 - [OpenApiv13adgroupcreateAudienceRuleExclusionsFilter](docs/OpenApiv13adgroupcreateAudienceRuleExclusionsFilter.md)
 - [OpenApiv13adgroupcreateAudienceRuleExclusionsFilterFilters](docs/OpenApiv13adgroupcreateAudienceRuleExclusionsFilterFilters.md)
 - [OpenApiv13adgroupcreateAudienceRuleExclusionsRules](docs/OpenApiv13adgroupcreateAudienceRuleExclusionsRules.md)
 - [OpenApiv13adgroupcreateAudienceRuleInclusions](docs/OpenApiv13adgroupcreateAudienceRuleInclusions.md)
 - [OpenApiv13adgroupcreateAudienceRuleInclusionsRules](docs/OpenApiv13adgroupcreateAudienceRuleInclusionsRules.md)
 - [OpenApiv13adgroupcreateExcludedCustomActions](docs/OpenApiv13adgroupcreateExcludedCustomActions.md)
 - [OpenApiv13adgroupcreateIncludedCustomActions](docs/OpenApiv13adgroupcreateIncludedCustomActions.md)
 - [OpenApiv13adgroupcreateTargetingExpansion](docs/OpenApiv13adgroupcreateTargetingExpansion.md)
 - [OpenApiv13adgroupupdateAudienceRule](docs/OpenApiv13adgroupupdateAudienceRule.md)
 - [OpenApiv13adgroupupdateAudienceRuleExclusions](docs/OpenApiv13adgroupupdateAudienceRuleExclusions.md)
 - [OpenApiv13adupdateCreatives](docs/OpenApiv13adupdateCreatives.md)
 - [OpenApiv13advertiserupdateQualificationImages](docs/OpenApiv13advertiserupdateQualificationImages.md)
 - [OpenApiv13bcadvertisercreateAdvertiserInfo](docs/OpenApiv13bcadvertisercreateAdvertiserInfo.md)
 - [OpenApiv13bcadvertisercreateBillingGroupInfo](docs/OpenApiv13bcadvertisercreateBillingGroupInfo.md)
 - [OpenApiv13bcadvertisercreateBillingInfo](docs/OpenApiv13bcadvertisercreateBillingInfo.md)
 - [OpenApiv13bcadvertisercreateContactInfo](docs/OpenApiv13bcadvertisercreateContactInfo.md)
 - [OpenApiv13bcadvertisercreateCustomerInfo](docs/OpenApiv13bcadvertisercreateCustomerInfo.md)
 - [OpenApiv13bcadvertisercreateQualificationInfo](docs/OpenApiv13bcadvertisercreateQualificationInfo.md)
 - [OpenApiv13creativeportfoliocreateAdvancedAudioInfo](docs/OpenApiv13creativeportfoliocreateAdvancedAudioInfo.md)
 - [OpenApiv13creativeportfoliocreateAdvancedGestureIcon](docs/OpenApiv13creativeportfoliocreateAdvancedGestureIcon.md)
 - [OpenApiv13creativeportfoliocreateBadgeImageInfo](docs/OpenApiv13creativeportfoliocreateBadgeImageInfo.md)
 - [OpenApiv13creativeportfoliocreateBadgePosition](docs/OpenApiv13creativeportfoliocreateBadgePosition.md)
 - [OpenApiv13creativeportfoliocreatePortfolioContent](docs/OpenApiv13creativeportfoliocreatePortfolioContent.md)
 - [OpenApiv13creativeportfoliocreateStickerParam](docs/OpenApiv13creativeportfoliocreateStickerParam.md)
 - [OpenApiv13pixelbatchBatch](docs/OpenApiv13pixelbatchBatch.md)
 - [PixelBatchBody](docs/PixelBatchBody.md)
 - [PixelContent](docs/PixelContent.md)
 - [PixelContext](docs/PixelContext.md)
 - [PixelContextAd](docs/PixelContextAd.md)
 - [PixelContextPage](docs/PixelContextPage.md)
 - [PixelContextUser](docs/PixelContextUser.md)
 - [PixelProperties](docs/PixelProperties.md)
 - [PixelTrackBody](docs/PixelTrackBody.md)
 - [PortfolioCreateBody](docs/PortfolioCreateBody.md)
 - [TargetingCategoryRecommendBody](docs/TargetingCategoryRecommendBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.

