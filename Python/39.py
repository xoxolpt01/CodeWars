'''
Given two integers a and b, which can be positive or negative,
find the sum of all the integers between and including them and return it.
If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
'''
def get_sum(a,b):
    #good luck!
    if a == b:
        return a or b
    if a > b:
        sum = 0
        for i in range(b, a+1):
            sum += i
        return int(sum)
    else:
        sum = 0
        for i in range(a, b+1):
            sum += i
        return int(sum)

print(get_sum(0,-1))