import re
escape_4 = re.compile(r'\\x[0123456789abcdef]{2}')
escape_2 = re.compile(r'\\\\|\\\"')

f = open("input.txt").readlines()

diff = 0

for string in f:
    esc_4 = len(re.findall(escape_4, string))
    esc_2 = len(re.findall(escape_2, string))
    n_mem = 2 + len(string)
    n_str = len(string) - esc_2 - 3 * esc_4
    diff += n_mem - n_str
print(diff)

print(sum(2+string.count('\\')+string.count('"') for string in f))
