import business_api_client
import requests
import json
import pandas as pd
import os
from constants import URL_ADVERTISER_IDS, URL_ADVERTISER_INFO
from datetime import date, timedelta

from dotenv import load_dotenv
load_dotenv()

access_token =  os.environ.get('ACCESS_TOKEN', '')
app_id = os.environ.get('APP_ID', '')
secret = os.environ.get('SECRET', '')
bc_id = os.environ.get('BC_ID', '')

response_advertiser_ids = requests.get(url=URL_ADVERTISER_IDS, headers={'Access-Token': access_token}, 
                                       params={'app_id': app_id, 'secret': secret})

api_report = business_api_client.ReportingApi()

advertiser_ids = response_advertiser_ids.json()['data']['list']

ad_ids = []
for advertiser in advertiser_ids:
    advertiser_id = advertiser['advertiser_id']
    ad_ids.append(advertiser_id)

response_advertiser_info = requests.get(url=URL_ADVERTISER_INFO, headers={'Access-Token': access_token}, 
                                        params={'advertiser_ids': json.dumps(ad_ids)})
response_advertiser_info = response_advertiser_info.json()['data']['list']

date_from = date.today().replace(day=1)
date_to = (date_from + timedelta(days=32)).replace(day=1) - timedelta(days=1)
metrics = [
    "spend", "clicks", "impressions",  
    "cost_per_result", "reach", "cpc", # cost_per_result: Cost
    "cpm", "ctr", "conversion", "cost_per_conversion" # cost_per_conversion: CPA
]

for advertiser_id in ad_ids:
    api_report_responses = api_report.report_integrated_get(advertiser_id=advertiser_id, report_type="BASIC", 
                                                            access_token=access_token, dimensions=["ad_id"], 
                                                            data_level="AUCTION_AD", metrics=metrics, 
                                                            start_date=date_from, end_date=date_to)
    
    for advertiser in response_advertiser_info:
        if 'owner_bc_id' in advertiser and advertiser['owner_bc_id'] == bc_id and \
            advertiser['advertiser_id'] == advertiser_id:
            
            if api_report_responses['data']['list'] == []:
                
                api_report_responses['data']['list'] = [
                    {
                        'Account Name': advertiser['name'],
                        'Account ID': advertiser['advertiser_id'],
                        'Clicks': 0,
                        'Impression': 0,
                        'Cost': 0,
                        'Reach': 0,
                        'CPC': 0,
                        'CPM': 0,
                        'CTR': 0,
                        'Conversion': 0,
                        'CPA': 0
                    }
                ]
            
            api_report_response_results = api_report_responses['data']['list']
            
            df = pd.DataFrame(api_report_response_results)
            df.rename(columns={'cost_per_result': 'cost', 'cost_per_conversion': 'cpa'}, inplace=True)
            df.to_csv('tiktok_business_report.csv', index=False)