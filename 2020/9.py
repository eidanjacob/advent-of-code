def can_sum(nums_to_add, value):
    for i in nums_to_add:
        for j in nums_to_add:
            if i + j == value and i != j:
                return True

    return False

def part1(nums, preamble): 
    last = nums[0:preamble]
    index = 25
    current_num = nums[preamble]
    while can_sum(last, current_num):
        index += 1
        last = nums[(index-preamble):index]
        current_num = nums[index]
    return current_num

def part2(nums, target):
    range_start = 0
    range_end = 2
    while sum(nums[range_start:range_end]) != target:
        if range_end == len(nums):
            range_start += 1
            range_end = range_start + 2
        else:
            range_end += 1
    print(min(nums[range_start:range_end]) + max(nums[range_start:range_end]))

with open("./input.txt") as f:
    numbers = [int(n) for n in f.readlines()]
    first_weakness = part1(numbers, 25)
    print(first_weakness)
    part2(numbers, first_weakness)
