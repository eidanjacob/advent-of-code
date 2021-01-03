import hashlib

door = "cxdnnyjw"

pw = ""
index = 0
while len(pw) < 8:
    to_hash = door + str(index)
    dig = hashlib.md5(to_hash.encode()).hexdigest()
    if dig[0:5] == "00000":
        pw += dig[5]
    index += 1

print(pw)

pw = ["_" for i in range(8)]
index = 0
while any([p == "_" for p in pw]):
    to_hash = door + str(index)
    dig = hashlib.md5(to_hash.encode()).hexdigest()
    if dig[0:5] == "00000" and dig[5].isdigit() and int(dig[5]) < 8:
        pw[int(dig[5])] = dig[6] if pw[int(dig[5])] == "_" else pw[int(dig[5])]
    index += 1

print("".join(pw))