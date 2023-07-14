'''
In this little assignment you are given a string
of space separated numbers, and have to return the
highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space,
and highest number is first.
'''

def from_str_to_lis(numbers):
    s = numbers.replace(' ', ',')
    i = 0
    new_ls = []
    while i < len(s):
        try:
            new_ls.append(int(s[i]))
            i += 1
        except:
            if s[i] == '-':
                new_ls.append(s[i]+s[i+1])
                i += 1
            else:
                pass
            i += 1
    return new_ls, s

def high_and_low(value):
    normal_list = from_str_to_lis(value)
    new_ls = []
    for j in normal_list:
         new_ls.append(int(j))
    new_ls.sort()
    return new_ls #f'{max(new_ls)} {min(new_ls)}'

print(from_str_to_lis("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
#print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

'''
Field
text = '1 22 35'
#text = text.replace(' ', ',')
ls = []
i = 0
while i < len(text):
    try:
        if i != ' ':
            ls.append(text[i]+text[i+1])
            i += 1
        else:
            ls.append(text[i])
            i += 1
    except:
        pass
        i += 1

print(max(text))
print(ls)

'''