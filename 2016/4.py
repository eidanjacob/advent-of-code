def get_sector_id(room):
    last_dash = len(room) - [char == "-" for char in room[::-1]].index(True) - 1
    room_code = room[:last_dash]
    chars = { char : 0 for char in "abcdefghijklmnopqrstuvwxyz" }
    for char in room_code:
        if char != "-":
            chars[char] += 1
    chars_sorted = list(chars.items())
    chars_sorted.sort(key = lambda item: ord(item[0]) - 1e6 * item[1])
    pred_checksum = "".join(c for c, n in chars_sorted[:5])
    sector, actual_checksum = room[(last_dash+1):].split("[")
    if actual_checksum[:-1] == pred_checksum:
        return int(sector), True
    else:
        return 0, False

print(sum([get_sector_id(x.strip())[0] for x in open("input.txt").readlines()]))

def get_room_name(room):
    sector_id, success = get_sector_id(room)
    if not success:
        return 0, "decoy"
    else:
        last_dash = len(room) - [char == "-" for char in room[::-1]].index(True) - 1
        room_name = ""
        for char in room[:last_dash]:
            if char == "-":
                room_name += char
            else:
                rot_char = chr(((ord(char) - ord("a") + sector_id) % 26) + ord("a"))
                room_name += rot_char
        return sector_id, room_name

for room in open("input.txt").readlines():
    s, n = get_room_name(room.strip())
    if "north" in n:
        print(s, n)