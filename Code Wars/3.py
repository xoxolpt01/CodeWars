def make_negative(number):
    if number < 0:
        return number
    elif number > 0:
        res = -1 * number
        return res
    elif number == 0:
        return 0

print(make_negative(42))
print(make_negative(0))
print(make_negative(-10))