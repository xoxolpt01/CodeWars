'''
Welcome. In this kata, you are asked to square every digit of
a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out,
because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    # here put type str
    string = str(num)
    ls = list(string)

    ls_1 = []
    for i in ls:
        if int(i) < 0:
            pass
        elif int(i) == float:
            pass
        else:
            square = int(i) ** 2
            ls_1.append(square)
            new_cont = []

            # running here each element in list ls and add result in ls_1
            for k in ls_1:
                # here every element ls_1 is int, need to change to srt to join them all
                a = str(k)
                new_cont.append(a)
            join = ''.join(new_cont)
            # After joined return an integer

    return int(join)

print(square_digits(1234))