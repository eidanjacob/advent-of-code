card_key, door_key = [int(n) for n in open("input.txt").readlines()[0:2]]

def transform(subject_number, last_ans):
    return (last_ans * subject_number) % 20201227

card_size = 0
card_public_key = 1
while card_key != card_public_key:
    card_size += 1
    card_public_key = transform(7, card_public_key)

door_size = 0
door_public_key = 1
while door_key != door_public_key:
    door_size += 1
    door_public_key = transform(7, door_public_key)

card_encryption_key = 1
door_encryption_key = 1
for i in range(door_size):
    door_encryption_key = transform(card_public_key, door_encryption_key)
for i in range(card_size):
    card_encryption_key = transform(door_public_key, card_encryption_key)
print(card_encryption_key, door_encryption_key)
