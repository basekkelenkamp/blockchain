from pprint import pprint
from time import sleep
from hasher import hash_mod10sha

import requests
import json
import sys
sys.setrecursionlimit(50000)


def main():

    # GET request for json json data
    try:
        r = requests.get("https://programmeren9.cmgt.hr.nl:8000/api/blockchain/next")
        response = r.json()
        pprint(response)
    except Exception as e:
        print(f"Could not fetch data. {e}")
        exit()

    unhashed_block = format_last_block(response["blockchain"])
    hashed_block = hash_mod10sha(unhashed_block)

    nonce = generate_valid_nonce(response, hashed_block, 0)
    sleep(1)

    try:
        url = "https://programmeren9.cmgt.hr.nl:8000/api/blockchain"
        res = send_response(url, nonce, "333ak")
        print(res)

    except Exception as e:
        print(f"Post failed: {e}")

    breakpoint()


def format_last_block(block):
    _hash = block["hash"]
    _nonce = block["nonce"]
    _timestamp = block["timestamp"]
    _transaction_data = block["data"][0]
    _transaction_data.pop("_id")

    data = "".join([str(value) for value in _transaction_data.values()])

    return f"{_hash}{data}{_timestamp}{_nonce}"


def generate_new_base_block(hash: str, transactions: list, timestamp: int):
    return f"{hash}{transactions['from']}{transactions['to']}{transactions['amount']}{transactions['timestamp']}{str(timestamp)} "


def generate_valid_nonce(block: str, hash: str, nonce: int):
    try:
        base_block_string = generate_new_base_block(
            hash, block["transactions"][0], block["timestamp"]
        )

        unhashed_string = f"{base_block_string}{nonce}"
        hashed = hash_mod10sha(unhashed_string)

        if hashed[:4] == '0000':
            print(f"Valid nonce found! '{nonce}'")
            return nonce

        print(f"Invalid nonce: '{nonce}', trying again..")
        return generate_valid_nonce(block, hash, nonce + 1)

    except RecursionError as e:
        print("Recursion error. Trying again after 2 seconds.")
        sleep(2)
        return generate_valid_nonce(block, hash, nonce + 1)


def send_response(url: str, nonce: int, name):
    data = {
        "nonce": str(nonce),
        "user": name
    }

    return requests.post(url, data)


if __name__ == "__main__":
    main()
