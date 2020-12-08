import hashlib

hash_key = "bgvyzdsv"
i = 0
while True:
    str2hash = hash_key + str(i)
    result = str(hashlib.md5(str2hash.encode()).hexdigest())
    if all([str(char) == "0" for char in result[:5]]):
        print("five zeros:", i)
        if result[5] == "0":
            print("six zeros:", i)
            break
        
    i += 1
