'''
Your task is to make a function that can take any
non-negative integer as an argument and return it with
its digits in descending order. Essentially, rearrange
the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
'''

def descending_order(num):
    list_num = sorted(list(str(num)))
    new_ls = []
    i = 0
    while i < len(list_num) + 1:
        new_ls.append(list_num[-i])

        i += 1
    new_ls.pop(0)

    return int(''.join(new_ls))

print(descending_order(56627))