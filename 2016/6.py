messages = [x.strip() for x in open("input.txt").readlines()]
char_by_pos = { x : { c : 0 for c in "abcdefghijklmnopqrstuvwxyz" } for x in range(len(messages[0]))}
for m in messages:
    for i, c in enumerate(m):
        char_by_pos[i][c] += 1

correct = []
for i in range(len(messages[0])):
    top_char = [char for char, count in char_by_pos[i].items() if count == max(char_by_pos[i].values())]
    correct += top_char

print("".join(correct))

correct = []
for i in range(len(messages[0])):
    top_char = [char for char, count in char_by_pos[i].items() if count == min(char_by_pos[i].values())]
    correct += top_char

print("".join(correct))