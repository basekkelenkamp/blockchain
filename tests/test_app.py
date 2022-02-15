import os
import sys

cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path + "/..")

import pytest
from fixtures import api_response
from src.app import format_last_block, generate_new_base_block, generate_valid_nonce
from src.hasher import hash_mod10sha

# run with: poetry run pytest -v -s

# input & expected result
format_block_fixture = [
    (
        api_response,
        "000078454c038871fa4d67b0022a30baaf25eaa231f8991b108e2624f052f3f8CMGT Mining CorporationBob PIKAB11548689513858154874778871610312",
    )
]

# input & expected result. 2 scenarios
hash_mod10sha_fixture = [
    (
        "text",
        "d0b3cb0cc9100ef243a1023b2a129d15c28489e387d3f8b687a7299afb4b5079"
    ),
    (
        "000078454c038871fa4d67b0022a30baaf25eaa231f8991b108e2624f052f3f8CMGT Mining CorporationBob PIKAB11548689513858154874778871610312",
        "00005d430ce77ad654b5309a770350bfb4cf49171c682330a2eccc98fd8853cf",
    ),
]

# Inputs: hash, transactions, timestamp, & expected output. 2 Scenarios
generate_base_fixture = [
    (
        "d0b3cb0cc9100ef243a1023b2a129d15c28489e387d3f8b687a7299afb4b5079",
        api_response["transactions"][0],
        api_response["timestamp"],
        "d0b3cb0cc9100ef243a1023b2a129d15c28489e387d3f8b687a7299afb4b5079CMGT Mining CorporationBas BOOTB115487477332611548748101396",
    ),
    (
        "00005d430ce77ad654b5309a770350bfb4cf49171c682330a2eccc98fd8853cf",
        api_response["transactions"][0],
        api_response["timestamp"],
        "00005d430ce77ad654b5309a770350bfb4cf49171c682330a2eccc98fd8853cfCMGT Mining CorporationBas BOOTB115487477332611548748101396",
    ),
]

# Input: block, hash, nonce, & expected output nonce
generate_nonce_fixture = [
    (
        api_response,
        "000078454c038871fa4d67b0022a30baaf25eaa231f8991b108e2624f052f3f8",
        10312,
        30076,
    )
]


@pytest.mark.parametrize("input, expected", format_block_fixture)
def test_format_last_block(input, expected):
    result = format_last_block(input["blockchain"])

    assert expected == result


@pytest.mark.parametrize("input, expected", hash_mod10sha_fixture)
def test_hash_mod10sha(input, expected):
    result = hash_mod10sha(input)

    assert expected == result


@pytest.mark.parametrize("hash, transactions, timestamp, expected", generate_base_fixture)
def test_generate_new_base_block(hash, transactions, timestamp, expected):
    result = generate_new_base_block(hash, transactions, timestamp)

    assert expected == result


@pytest.mark.parametrize("block, hash, nonce, expected_nonce", generate_nonce_fixture)
def test_generate_valid_nonce(block, hash, nonce, expected_nonce):
    result = generate_valid_nonce(block, hash, nonce)

    assert expected_nonce == result
