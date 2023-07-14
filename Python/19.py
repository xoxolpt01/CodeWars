'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members
which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input:
Input will consist of a list of pairs. Each pair contains information for a single potential member.
Information consists of an integer for the person's age and an integer for the person's handicap.

Output:
Output will consist of a list of string values
(in Haskell and C: Open or Senior) stating whether the respective member is to be placed
in the senior or open category.

Example:
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
'''



def open_or_senior(data):
    i = 0
    new_ls = []
    while i < len(data):
        if data[i][0] >= 55:
            if data[i][1] > 7:
                new_ls.append('Senior')
            else:
                new_ls.append('Open')
        else:
            new_ls.append("Open")


        i += 1
    return new_ls



data = [(45, 12),(55,21),(19, -2),(104, 20)]
print(open_or_senior(data))