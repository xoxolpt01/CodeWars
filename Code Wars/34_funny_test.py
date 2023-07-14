'''
Some numbers have funny properties. For example:
89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... :
(a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits
of n taken to the successive powers of p is equal to k * n.
In other words:

Is there an integer k such as :
(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.
Note: n and p will always be given as strictly positive integers.
'''


def dig_pow(n, p):
    # your code
    n = str(n)
    i = 0
    sum = 0
    while i < len(n):
        sum += int(n[i])**(i+p)
        i += 1
    #return int(sum/int(sum / int(n)))

    #print(sum)# sum = 13 ====>  dig_pow(92, 1)
    # if int(sum / int(sum / int(n))) == int(n):
    #     return int(sum / int(n))
    # elif int(sum / int(sum / int(n))) != int(n):
    #     return -1
    try:
        if int(sum/int(sum/int(n))) == int(n):
            return int(sum/int(n))
        elif int(sum/int(sum/int(n))) != int(n):
            return -1
    # If will return mistake about 0
    except:
        return -1

print('True', dig_pow(46288, 3)) # 51
print('True', dig_pow(54, 5)) # 25
print('False = -1', dig_pow(92, 1)) # -1
print('True', dig_pow(8, 3)) # 64

'''
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''