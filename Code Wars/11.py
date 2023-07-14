'''
Create a function that returns the sum of the two
lowest positive numbers given an array of minimum 4 positive
integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], t
he output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''


ls = [19, 5, 42, 2, 77, -2, 0]

ls.sort()
new_ls = []
#neg_ls = []

i = 0
while i <= len(ls):
    if ls[i] > 0:
        new_ls.append(ls[i])
        if len(new_ls) == 2:
            break
    i += 1

print(new_ls)
print(new_ls[0]+new_ls[1])


