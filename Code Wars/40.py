'''
lock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since
midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

def past(h, m, s):
    # Good Luck!
    # 1 sec = 1000 mlsc
    return (((h*60)*60)*1000)+((m*60)*1000)+ (s*1000)

print(past(0, 1, 1))
print(past(1,1,1))
print(past(0,0,0))
print(past(1,0,1))
print(past(99,59,59))