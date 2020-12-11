with open("input.txt") as f:
    strings = f.readlines()
    nice = 0
    for string in strings:
        if sum([1 for i in string if i in "aeiou"]) >= 3:
            if any([string[i] == string[i-1] for i in range(1,len(string))]):
                if not any([string[i:(i+2)] in ["ab", "cd", "pq", "xy"] for i in range(1, len(string))]):
                    nice += 1

    print(nice)

    nice = 0
    for string in strings:
        repeats_without_overlapping = False
        checked_pairs = set()
        for i in range(len(string)):
            this_pair = string[i:i+2]
            if this_pair in checked_pairs:
                continue
            same_pair = [this_pair == string[j:j+2] for j in range(i, len(string))]
            repeats_without_overlapping = repeats_without_overlapping or any([(not same_pair[j]) and same_pair[j+1] for j in range(len(same_pair)-1)]) or any(same_pair[2:])
            if repeats_without_overlapping:
                break
            checked_pairs.add(this_pair)
            
        repeats_one_between = False
        checked_letters = set()
        for i in range(len(string)):
            this_letter = string[i]
            if this_letter in checked_letters:
                continue
            same_letter = [this_letter == d for d in string[i:]]
            repeats_one_between = repeats_one_between or any([same_letter[j] and same_letter[j+2] for j in range(len(same_letter)-2)])
            if repeats_one_between:
                break
            checked_letters.add(this_letter)
            
        nice += 1 if repeats_one_between and repeats_without_overlapping else 0

    print(nice)
