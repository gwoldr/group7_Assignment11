"""
Name: Group 7
Email: groenern@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Using an API key and JSON to get data from an API 
Anything Else: No problems setting up project
"""
# groenern API-KEY: 4vbiCOIQc2fDQeSlS0kzkJV6fKZg2s6qNPiXayCk

import json
import requests

def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)
                    
# build url data request 
apiKey = 'EgnxSAjZLszEJuhOkNovSKbMn7prxKROhYjfg5Ui'

url = "https://api.data.gov/ed/collegescorecard/v1/schools?"
url = f"{url}api_key={apiKey}&fields=school.name,id,school.state&page=25&_per_page=100"

# json magic to get data
data = requests.get(url).json()

for result in data.get('results', []):
  print(result)
  
