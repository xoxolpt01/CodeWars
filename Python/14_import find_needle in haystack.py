'''
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
Note: In COBOL, it should return "found the needle at position 6"

'''


def find_needle(haystack):
    for i in haystack:
        if i == 'needle':
            return "found the needle at position %d" % haystack.index(i)

ls = ['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']
ls_1 = [153, 173, 233, 80, 118, 37, 71, 137, 247, 11, 82, 68, 176, 9, 215, 202, 248, 44, 253, 118, 288, 49, 289, 171, 147, 135, 65, 49, 186, 91, 264,
        72, 260, 222, 223, 97, 10, 47, 14, 197, 143, 286, 155, 221, 54, 24, 193, 17, 115, 15, 5, 147, 7, 154, 281, 179, 108, 56, 12, 19, 275, 297, 56,
        'needle', 105, 103, 187, 181, 75, 47, 5, 121, 23, 271, 106, 8, 80, 83, 217, 158, 49, 152, 99, 87, 132, 20, 13, 132, 60, 101, 12, 239, 259,
        139, 110, 158, 55, 132, 175, 141]

ls_2 = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(ls_2))