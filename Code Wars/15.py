def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        r = (year // 100) + 1
        return r

print('1705 ->', century(1755))
print()
print('1900 ->', century(1900))
print()
print('2000 ->', century(2000))
print()
print('356 ->', century(356))
print()
print('89 ->', century(89))