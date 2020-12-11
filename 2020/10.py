with open("input.txt") as f:
    jolts = [0] + [int(n) for n in f.readlines()]
    jolts.sort()
    diffs = [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]
    one_diffs = sum([1 for i in diffs if i == 1])
    three_diffs = sum([1 for i in diffs if i == 3]) + 1
    print(one_diffs * three_diffs)
    
    unique_arrs_after_index = {len(jolts)-1 : 1}
    def n_unique_arrangements(index):
        if index in unique_arrs_after_index:
            return unique_arrs_after_index[index]
        n_to_return = 0
        for i, jolt in enumerate(jolts[index+1:]):
            if jolt - jolts[index] > 3:
                break
            n_to_return += n_unique_arrangements(index+i+1)
        unique_arrs_after_index[index] = n_to_return
        return n_to_return

    print(n_unique_arrangements(0))
