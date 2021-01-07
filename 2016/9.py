compressed_data = open("input.txt").read().strip()

def decompress_1(string):
    if "(" in string:
        paren_index = string.index("(")
        if ")" in string[paren_index:]:
            close_paren_index = string.index(")")
            paren_exp = string[(paren_index + 1):close_paren_index].split("x")
            if len(paren_exp) == 2 and all([s.isnumeric() for s in paren_exp]):
                n_chars, repetitions = [int(n) for n in paren_exp]
                after_repeat = decompress_1(string[(close_paren_index + 1 + n_chars):])
                return paren_index + n_chars * repetitions + after_repeat
    return len(string)

exp_string = decompress_1(compressed_data)
print(exp_string)

def decompress_2(string):
    if "(" in string:
        paren_index = string.index("(")
        if ")" in string[paren_index:]:
            close_paren_index = string.index(")")
            paren_exp = string[(paren_index + 1):close_paren_index].split("x")
            if len(paren_exp) == 2 and all([s.isnumeric() for s in paren_exp]):
                n_chars, repetitions = [int(n) for n in paren_exp]
                repeated = decompress_2(string[(close_paren_index + 1):(close_paren_index + 1 + n_chars)]) * repetitions
                after_repeat = decompress_2(string[(close_paren_index + 1 + n_chars):])
                return paren_index + repeated + after_repeat
    return len(string)

exp_string = decompress_2(compressed_data)
print(exp_string)