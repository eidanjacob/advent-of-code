seq = "1321131112"

for i in range(50):
    new_seq = ""
    index = 0
    while index < len(seq):
        digit = seq[index]
        multiplicity = 1
        if index + 1 < len(seq):
            while seq[index + 1] == digit:
                index += 1
                multiplicity += 1
                if index + 1 >= len(seq):
                    break
        new_seq += str(multiplicity) + digit
        index += 1
    seq = new_seq

print(len(seq))
