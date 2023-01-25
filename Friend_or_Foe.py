""""
Friend_or_Foe.py
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
"""

'''first solution'
def friend(x):
    result = []
    for i in x:
         if len(i) == 4:
            result.append(i)
    return result
'''
def friend(my_list):
    for i in list(my_list):
        if len(i) != 4:
            my_list.remove(i)
    return my_list

# note: if you remove an element during the loop, the index auto-adjusts on the spot, and the next element will be skipped
# if you want to maintain the correct loop, use range for looping the list, or iterate through a temporary copy

print(friend(["Ryan", "mimi", "Kieran", "Jason", "Yous"]))
