'''
codewars.com
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
'''


def functie(y):
    # print (y)
    sum = 0
    for i in y:
        c = 0
        for z in y:
            if i == z:
                c = c + 1
        if c == 1:
            sum = sum + i
    return sum
    # print (sum)


x = (4, 5, 7, 5, 4, 8)
print(functie(x))