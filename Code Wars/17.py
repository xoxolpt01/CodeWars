def filter_list(l):
    print(len(l))
    filtered_list = []
    for i in l:
        if type(i) == str:
            pass
        elif type(i) == int:
            if i < 0:
                pass
            else:
                filtered_list.append(i)
    return filtered_list


print(filter_list([1,2,'a','123']))