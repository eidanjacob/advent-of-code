def pass_part_1(password):
    for char in ["i", "o", "l"]:
        if char in password:
            return False

    pairs = False
    for i in range(5):
        if password[i] == password[i+1]:
            for j in range(i+2, 7):
                if password[j] == password[j+1]:
                    pairs = True
                    break
        if pairs:
            break
            
    if not pairs:
        return False
    
    straight = False
    for i in range(6):
        one, two, three = password[i], password[i+1], password[i+2]
        if ord(one) + 1 == ord(two) and ord(two) + 1 == ord(three):
            straight = True
            break
    return straight

def increment(password, index = 7):
    if password[index] == "z":
        return increment(password, index - 1) + "a"
    else:
        return password[0:index] + chr(ord(password[index])+1)

password = "hxbxwxba"
while not pass_part_1(password):
    password = increment(password)

print(password)
password = increment(password)
while not pass_part_1(password):
    password = increment(password)

print(password)
