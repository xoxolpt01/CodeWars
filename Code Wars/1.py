# def count_sheep(n):
#     # your code
#     if n < 0:
#         n = -1* n
#     elif n == 0:
#         n += 1
#     for i in range(n+1):
#         print('%d sheep...' % i, end='')
#         i += 1
#     return
# print(count_sheep(5))

def count_sheep(n):
    if n < 0:
        n *= -1
    s = ""
    if n == 0:
        return s
    for i in range(1, n+1):
        s += f"{i} sheep... "
    return s
print(count_sheep(5))