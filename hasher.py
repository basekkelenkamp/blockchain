def hash_mod10sha(input):
    no_space = input.replace(' ', '')
    ascii_values = [character if character.isdigit() else ord(character) for character in no_space]

    combined_values = []
    for value in ascii_values:
        for digit in str(value):
            combined_values.append(int(digit))

    chunk_values = split_into_chunks(combined_values, 10)
    filled_values = add_to_last_element(chunk_values)

    breakpoint()
    return input


def split_into_chunks(li: list, chunk: int):
    if len(li) < chunk:
        return li
    return [li[i:i+chunk] for i in range(0, len(li), chunk)]


def add_to_last_element(input: list):
    li = list(range(10))
    number_to_add = 10 - len(input[-1])

    input[-1].extend(li[:number_to_add])
    return input
