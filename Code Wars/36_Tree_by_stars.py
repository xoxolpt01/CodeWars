'''
Build a pyramid-shaped tower, as an array/list of strings,
given a positive integer number of floors.
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ",
  "*****"
]


And a tower with 6 floors looks like this:
[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
'''
def tower_builder(n_floors):
    # build here
    ls = []
    i = 1
    while i <= n_floors:
        ls.append((n_floors-i)*' '+(2*i-1)*'*'+(n_floors-i)*' ')
        i += 1
    return ls
print(tower_builder(6))