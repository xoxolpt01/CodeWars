'''
Given an array of integers.

Return an array, where the first element i
s the count of positives numbers and the second element is sum of negative numbers.
0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ---> [10,-65])
([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) ----> [8,-50])
([1]) ----> [1,0])
([-1]) ----> [0,-1])
([0,0,0,0,0,0,0,0,0])----> [0,0])
([]) -----> [])


'''



def count_positives_sum_negatives(arr):
    check = 0
    if arr == None:
        print('None_0')
        return []

    elif arr == []:
        print('pr_[]')
        return []

    elif len(arr) > 0:
        new_list = []
        sum_pos = 0
        sum_neg = 0
        for i in arr:
            if i > 0:
                sum_pos += 1
            elif i < 0:
                sum_neg += i

        new_list.append(sum_pos)
        new_list.append(sum_neg)
        print('New_list')
        return new_list

print(count_positives_sum_negatives([0,0,0,0,0]))