
'''Write a small function that returns the values of an array that are not odd.
All values in the array will be integers. Return the good values in the order they are given.
codewars.com
'''

def no_odds(values):
    new_values = []
    for i in values:
        if (i % 2) == 0:
            new_values.append(i)
    return new_values


my_array = [1, 3, 6, 2, 8, 9]
no_odds(my_array)

'''
other solutions:
def no_odds(values):
    return [i for i in values if i % 2 == 0]
'''