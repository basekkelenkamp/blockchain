import os
import sys

cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path + "/..")

import pytest
from fixtures import api_response
from src.hasher import hash_mod10sha, merge_lists, add_to_last_element

# run with: poetry run pytest -v -s

# input & expected result. 4 scenarios
add_to_last_element_fixture = [
    (
        [[3, 5, 7, 3, 6, 8, 2, 6, 5, 7], [0, 5, 7, 3, 2, 8, 2, 6, 5, 7], [0, 5, 2]],
        [[3, 5, 7, 3, 6, 8, 2, 6, 5, 7], [0, 5, 7, 3, 2, 8, 2, 6, 5, 7], [0, 5, 2, 0, 1, 2, 3, 4, 5, 6]],
    ),
    (
        [[6, 4]],
        [[6, 4, 0, 1, 2, 3, 4, 5, 6, 7]]
    ),
    (
        [[3, 7, 8, 7, 2, 0, 1, 3, 7, 2], [1]],
        [[3, 7, 8, 7, 2, 0, 1, 3, 7, 2], [1, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
    ),
    (
        [[0, 4, 6, 2, 1, 5, 1, 5, 9]],
        [[0, 4, 6, 2, 1, 5, 1, 5, 9, 0]]
    )
]


# input & expected result. 2 Scenarios
merge_lists_fixture = [
    (
        [[3, 5, 7, 3, 6, 8, 2, 6, 5, 7], [0, 5, 7, 3, 2, 8, 2, 6, 5, 7], [0, 5, 2, 0, 1, 2, 3, 4, 5, 6]],
        [3, 5, 6, 6, 9, 8, 7, 6, 5, 0]
    ),
    (
        [[6, 4, 0, 1, 2, 3, 4, 5, 6, 7]],
        [6, 4, 0, 1, 2, 3, 4, 5, 6, 7]
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


@pytest.mark.parametrize("input, expected", add_to_last_element_fixture)
def test_add_to_last_element(input, expected):
    result = add_to_last_element(input)

    assert len(result[-1]) == 10
    assert expected == result


@pytest.mark.parametrize("input, expected", merge_lists_fixture)
def test_merge_lists(input, expected):
    result = merge_lists(input)

    assert expected == result


@pytest.mark.parametrize("input, expected", hash_mod10sha_fixture)
def test_hash_mod10sha(input, expected):
    result = hash_mod10sha(input)

    assert expected == result
