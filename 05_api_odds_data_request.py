print('\n\n ---------------- START ---------------- \n')

import time
start=time.time()

import requests
import pandas as pd
import math
from os import listdir
import json

api_key = (open('api_key.txt', mode='r')).read()
regions = "uk,eu"

def get_api_data(base_url, end_url):
    url = base_url + end_url
    res = requests.get(url, params = {
         'api_key': api_key,
         'regions': regions,
    })
    if res.status_code != 200:
        raise RuntimeError(f'error {res.status_code}')
    res_t = res.text
    return res_t

def save_api_output(save_name, jason_data, json_data_path=''):
    writeFile = open(json_data_path + save_name + '.json', 'w')
    writeFile.write(jason_data)
    writeFile.close()
    
    
def read_json_as_pd_df(json_data, json_data_path='', orient_def='records'):
    output = pd.read_json(json_data_path + json_data, orient=orient_def)
    return output


base_url = "https://api.the-odds-api.com/v4/"


odds_data = get_api_data(base_url , f'sports/soccer_epl/odds')

save_api_output(f'2023_live_odds_data', odds_data, json_data_path = 'live_odds_data/')

live_odds_data_df = read_json_as_pd_df(f'2023_live_odds_data.json', json_data_path='live_odds_data/')

print(live_odds_data_df)


