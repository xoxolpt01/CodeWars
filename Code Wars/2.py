def smash(words):
    a = " "
    s = ''
    for i in ls:
        s += i + ' '

    s = s.rstrip(a)
    return s
ls = ['hello', 'world', 'this', 'is', 'great']

# def smach(words):
#     s = ''
#     a = " "
#     for i in range(len(words)):
#         s += words[i] + " "
#     s = s.rstrip(a)
#     return s

print(smash(ls))