'''
Task
Given an integral number, determine if it's a square number:

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false

'''


def square_1(alpha):
    if alpha < 0:
        return False
    else:
        i = 0
        while i <= alpha:
            sqrt = i ** 2
            if sqrt == alpha:
                print('root %d is' % alpha, i)
                return True
            elif sqrt > alpha:
                print(alpha, 'None square number')
                #print('2nd False')
                return False
            else:
                i += 1

print(square_1(26))