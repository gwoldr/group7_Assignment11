'''
Created on Nov 3, 2022

@author: Roman
'''
# groenern API-KEY: 4vbiCOIQc2fDQeSlS0kzkJV6fKZg2s6qNPiXayCk

import json
import requests

response = requests.get('https://api.fda.gov/drug/event.json?api_key=4vbiCOIQc2fDQeSlS0kzkJV6fKZg2s6qNPiXayCk')
json_string = response.content
  
parsed_json = json.loads(json_string) # Now we have a python dictionary
  
#print(parsed_json)
#print(parsed_json['data'][0]['description'])
#print(parsed_json['data'][0]['directionsInfo'])
  
total = int(parsed_json['total'])        # The number of parks that were returned

for park in parsed_json['data']:
    print (park)