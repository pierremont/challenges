'''Thinkful - List and Loop Drills: Lists of lists (codewars.com, 7kyu)
You have a two-dimensional list in the following format:
data = [[2, 5], [3, 4], [8, 7]]
Each sub-list contains two items, and each item in the sub-lists is an integer.
Write a function process_data()/processData() that processes each sub-list like so:
    [2, 5] --> 2 - 5 --> -3
    [3, 4] --> 3 - 4 --> -1
    [8, 7] --> 8 - 7 --> 1
and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.
For input, you can trust that neither the main list nor the sublists will be empty.'''

def process_data(data):
    result = 1
    for i in data:
        result = result * (i[0] - i[1])
    return result

data = [[2, 5], [3, 4], [8, 7]]
print(process_data(data))

'''other solutions;
def process_data(data):
    product = 1
    for tuple in data:
        product *= tuple[0] - tuple[1] 
    return product 
    
from math import prod
def process_data(data):
    return prod(i[0] - i[1] for i in data)
    
from math import prod
def process_data(data):
    return prod(a - b for a, b in data)'''

