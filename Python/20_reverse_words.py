def solution(string):
    new_ls = []
    last = ''
    for i in string:
        new_ls.append(i)
    new_ls.reverse()
    return last.join(new_ls)

print(solution('sometimes'))
