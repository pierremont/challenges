
'''
Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.
'''

def maps(a):
    result = []
    for i in a:
        result.append(i*2)
    return result

entry = maps([2, 4, 323])
print entry

'''
def maps(a):
    return a * 2

x = map(maps, (5, 6))
print(list(x))'''