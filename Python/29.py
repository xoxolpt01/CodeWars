'''
Ben has a very simple idea to make some profit: he buys something and sells it again.
Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price.
Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]
'''

def min_max(lst):
    new = []
    if len(lst) == 1:
        return [lst[0], lst[0]]
    else:
        new.append(min(lst))
        new.append(max(lst))
        return new

print(min_max([1,2,3,4,5]))
print(min_max([1]))
