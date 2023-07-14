def sum_array(a):
    sum = 0
    for i in a:
        sum += i

    return sum

s = [1, 5.2, 4, 0, -1]
print(sum_array(s))