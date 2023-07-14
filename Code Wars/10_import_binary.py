'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)


'''


def add_binary(a, b):
    txt = bin(int(a) + int(b))
    txt_1 = list(txt)
    txt_1.pop(0)
    txt_1.pop(0)
    #print(txt_1)
    #print(type(txt_1[0]))
    s = "".join(txt_1)
    return s

print(add_binary(57,12))