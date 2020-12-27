import json

data = json.load(open("input.txt"))

def sum_numbers(obj):
    total = 0
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                total += sum_numbers(v)
            elif isinstance(v, int):
                total += v
    elif isinstance(obj, list):
        for item in obj:
            total += sum_numbers(item)
    elif isinstance(obj, int):
        return obj
    return total

print(sum_numbers(data))

def sum_nonred(obj):
    total = 0
    if isinstance(obj, dict):
        for k, v in obj.items():
            if v == "red":
                return 0
            elif isinstance(v, (dict, list)):
                total += sum_nonred(v)
            elif isinstance(v, int):
                total += v
    elif isinstance(obj, list):
        for item in obj:
            total += sum_nonred(item)
    elif isinstance(obj, int):
        return obj
    return total

print(sum_nonred(data))
print(data)
