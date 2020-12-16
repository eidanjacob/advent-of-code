nums = [2,0,6,12,1,3]
turn_last_spoken = { num : i for i, num in enumerate(nums[:-1])}
last_turn = nums[-1]
for i in range(len(nums), 30000000):
    this_turn = 0
    if last_turn in turn_last_spoken.keys():
        this_turn = i - 1 - turn_last_spoken[last_turn]
        turn_last_spoken[last_turn] = i - 1
    else:
        turn_last_spoken[last_turn] = i - 1
    last_turn = this_turn
    if i == 2019:
        print(this_turn)
        
print(last_turn)
