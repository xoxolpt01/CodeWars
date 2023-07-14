'''
Write a function, persistence, that takes in a
positive parameter num and returns its multiplicative
persistence, which is the number of times you must multiply
the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''

def persistence(n):

    def calc(x):
        i = 0
        res = 1
        while i < len(str(x)):
            res *= int(str(x)[i])
            i += 1
        return res
    if len(str(calc(n))) == 1:
        return

    return

print(persistence(39))


'''
test.assert_equals(persistence(39), 3)
test.assert_equals(persistence(4), 0)
test.assert_equals(persistence(25), 2)
test.assert_equals(persistence(999), 4)
'''