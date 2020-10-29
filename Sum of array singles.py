'''
codewars.com
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
'''

#initially i used 2 loops, but that was optimized, since it was rejected by codewars (even though it worked)

def functie(arr):
    temp_arr = []
    sum = 0
    for i in arr:
        if i in temp_arr: #create a temporary list from which you subtract the item if it's already there
            sum -= i
        else:
            sum += i
            temp_arr.append(i)
    return sum

arr = (4, 5, 7, 5, 4, 8)
print(functie(arr))

'''other solutions from codewars:
===============
def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])
===============
from collections import Counter

def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)
'''