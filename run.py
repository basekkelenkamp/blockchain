from pprint import pprint

import requests
import json

# get json json data
r = requests.get('https://programmeren9.cmgt.hr.nl:8000/api/blockchain/next')
response = r.json()
pprint(response)

breakpoint()
