from hashlib import sha256
from pprint import pprint

from hasher import hash_mod10sha
from util.util import merge_strings

import requests
import json

# GET request for json json data
r = requests.get('https://programmeren9.cmgt.hr.nl:8000/api/blockchain/next')
response = r.json()
pprint(response)

# hash last block in chain
# last_hash = response['blockchain']['hash']
# last_nonce = response['blockchain']['nonce']
# last_timestamp = response['blockchain']['timestamp']
# bc_transaction_timestamp = response['blockchain']['data'][0]['timestamp']
#
# hashed = merge_strings(bc_hash, bc_transaction_timestamp, bc_nonce)




def format_last_block(block):
    _hash = block['hash']
    _nonce = block['nonce']
    _timestamp = block['timestamp']
    _transaction_data = block['data'][0]
    _transaction_data.pop('_id')

    data = ''.join([str(value) for value in _transaction_data.values()])

    return f"{_hash}{data}{_timestamp}{_nonce}"


unhashed_block = format_last_block(response['blockchain'])
hashed_block = hash_mod10sha(unhashed_block)


breakpoint()
