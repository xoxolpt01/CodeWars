def invert(lst):
    new_ls = []
    if lst == []:
        return []
    for i in lst:
        new_ls.append(i*(-1))
    return new_ls
print(invert([-1,2,-3,4,-5]))