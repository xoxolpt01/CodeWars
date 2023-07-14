'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
'''


def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'R':
        name = name + " plays banjo"
    elif name[0] == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name

print(are_you_playing_banjo('So'))