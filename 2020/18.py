problems = [p.replace("\n", "").split(" ") for p in open("input.txt").readlines()]

def part1(problem):
    if len(problem) == 1:
        return int(problem[0])
    if ")" in problem[-1]:
        sub_problem = [problem[-1]]
        n_open = sum([1 for char in problem[-1] if char == ")"])
        index = -2
        while n_open > 0:
            if ")" in problem[index]:
                n_open += sum([1 for char in problem[index] if char == ")"])
            elif "(" in problem[index]:
                n_open -= sum([1 for char in problem[index] if char == "("])
            sub_problem.append(problem[index])
            index -= 1
        sub_problem.reverse()
        sub_problem[0] = sub_problem[0][1:]
        sub_problem[-1] = sub_problem[-1][:-1]
        if len(sub_problem) == len(problem):
            return part1(sub_problem)
        else:
            return (part1(sub_problem) * part1(problem[:(index)])) if problem[index] == "*" else (part1(sub_problem) + part1(problem[:(index)]))
    else:
        right_val = int(problem[-1])
        return (right_val * part1(problem[:-2])) if problem[-2] == "*" else (right_val + part1(problem[:-2]))

print(sum([part1(problem) for problem in problems]))

def make_sub_problems(problem):
    cp = problem.copy()
    for i in range(1, len(problem), 2):
        if ")" not in problem[i - 1] and problem[i] == "+":
            j = i + 2
            if ")" in problem[i+1]:
                cp[i - 1] = "(" + cp[i - 1]
                cp[j - 1] = cp[j - 1] + ")"
                continue
            n_open = sum([1 for char in problem[i + 1] if char == "("])
            paren_exp = n_open > 0
            while j < len(problem):
                if n_open < 0:
                    break
                elif paren_exp:
                    n_open += sum([1 for char in problem[j + 1] if char == "("])
                    n_open -= sum([1 for char in problem[j + 1] if char == ")"]) 
                    paren_exp = n_open > 0
                    if not paren_exp:
                        j += 2
                        break
                else:
                    if problem[j] == "*":
                        break
                    n_open += sum([1 for char in problem[j + 1] if char == "("])
                    n_open -= sum([1 for char in problem[j + 1] if char == ")"])
                    paren_exp = n_open > 0
                j += 2
            cp[i - 1] = "(" + cp[i - 1]
            cp[j - 1] = cp[j - 1] + ")"
        elif ")" in problem[i - 1] and problem[i] == "+":
            j = i - 2
            n_open = sum([1 for char in problem[i - 1] if char == ")"])
            while j > 0:
                n_open += sum([1 for char in problem[j - 1] if char == ")"])
                n_open -= sum([1 for char in problem[j - 1] if char == "("])
                if n_open < 1:
                    break
                j -= 2
            if "(" not in problem[i + 1]:
                cp[i + 1] = cp[i + 1] + ")"
                cp[j - 1] = "(" + cp[j - 1]
            else:
                k = i + 2
                n_open = sum([1 for char in problem[i + 1] if char == "("])
                while k < len(problem):
                    n_open += sum([1 for char in problem[k + 1] if char == "("])
                    n_open -= sum([1 for char in problem[k + 1] if char == ")"])
                    if n_open < 1:
                        break
                    k += 2
                cp[k + 1] = cp[k + 1] + ")"
                cp[j - 1] = "(" + cp[j - 1]
    return cp
        

def part2(problem):
    prob = make_sub_problems(problem)
    return(eval(" ".join(prob)))
    
                                
print(sum([part2(p) for p in problems]))
