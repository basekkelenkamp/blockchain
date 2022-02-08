from hashlib import sha256


def hash_mod10sha(input):
    no_space = input.replace(" ", "")
    ascii_values = [
        character if character.isdigit() else ord(character) for character in no_space
    ]

    combined_values = []
    for value in ascii_values:
        for digit in str(value):
            combined_values.append(int(digit))

    chunk_values = split_into_chunks(combined_values, 10)
    filled_values = add_to_last_element(chunk_values)
    final_values = merge_lists(filled_values)

    string_value = "".join([str(value) for value in final_values])
    return sha256(string_value.encode("utf-8")).hexdigest()


def split_into_chunks(li: list, chunk: int):
    if len(li) < chunk:
        return li
    return [li[i : i + chunk] for i in range(0, len(li), chunk)]


def add_to_last_element(input: list):
    li = list(range(10))
    number_to_add = 10 - len(input[-1])

    input[-1].extend(li[:number_to_add])
    return input


def merge_lists(input: list):
    if len(input) == 1:
        return input[0]

    merged_list = [
        (input[0][index] + input[1][index]) % 10 for index, li in enumerate(input[0])
    ]

    del input[:2]
    input.insert(0, merged_list)

    return merge_lists(input)
