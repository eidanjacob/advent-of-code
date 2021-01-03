target_row = 3010
target_col = 3019

current_row = 1
current_col = 1
next_row = 2

code = 20151125

while target_row != current_row or target_col != current_col:
    code = (code * 252533) % 33554393
    if current_row == 1:
        current_row = next_row
        next_row += 1
        current_col = 1
    else:
        current_row -= 1
        current_col += 1

print(code)