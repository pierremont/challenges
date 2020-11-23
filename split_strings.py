'''Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
www.codewars.com
'''

def split(word):
    my_list = []
    final_list = []
    my_list[:0] = word
    for i in range(len(my_list)):
        if (i % 2) == 0:
            final_list.append(my_list[i])
        else:
            final_list[len(final_list) - 1] += my_list[i]
    if (len(my_list) % 2) != 0:
        final_list[len(final_list) - 1] += "_"
    return final_list


print(split('abcde'))


'''other solutions:
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
===================
import re

def solution(s):
    return re.findall(".{2}", s + "_")
'''


''' outputs 0, 1, 2:
for i in range(3):
    print(i)
'''