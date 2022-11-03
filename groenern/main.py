'''
Created on Nov 3, 2022

@author: Roman
'''
# groenern API-KEY: 4vbiCOIQc2fDQeSlS0kzkJV6fKZg2s6qNPiXayCk

import json
import requests

URL = 'https://api.fda.gov/drug/event.json?api_key=4vbiCOIQc2fDQeSlS0kzkJV6fKZg2s6qNPiXayCk'
data = requests.get(URL).json()

for result in data.get('results', []):
  print(result)

