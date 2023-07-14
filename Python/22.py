'''
Write a function to convert a name into initials.
This kata strictly takes two words with one space in between them.

The output should be two capital letters with a
dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F


'''


def abbrev_name(name):
    new_ls = []
    new_ls.append(name[0])
    for i in name:
        if ord(i) == 32:
            s = list(name).index(' ')
            new_ls.append(name[s+1])
    if 65 <= ord(new_ls[0])<= 90:
        new = ord(new_ls[0])
    else:
        new = ord(new_ls[0]) - 32

    if 65 <= ord(new_ls[1])<= 90:
        new_1 = ord(new_ls[1])
    else:
        new_1 = ord(new_ls[1]) - 32

    i = 0
    while i <= 1:
        new_ls.pop(0)
        i += 1
    new_ls.insert(0, chr(new))
    new_ls.insert(1,chr(new_1))
    new_ls.insert(1,'.')
    abbrev = ''.join(new_ls)
    return abbrev



print(abbrev_name("ryfaiP JOCmwc"))
#Sam Harris => S.H