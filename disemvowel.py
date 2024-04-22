#*7 kyu, # /* Disemvowel Trolls https://www.codewars.com/kata/52fba66badcd10859f00097e/train/java
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    final_text = ''
    for i in string_:
        if i.lower() not in ('a', 'e', 'i', 'o', 'u'):
            final_text = final_text + i
    return final_text

text = "This website is for losers LOL!"
result = disemvowel(text)
print(result)

# OTHER SOLUTIONS:
# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s
=========
# import re
# def disemvowel(string):
#     return re.sub(r"[aeiouAEIOU]", "", string)