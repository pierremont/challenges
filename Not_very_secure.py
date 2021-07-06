''' Not very secure
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
The string has the following conditions to be alphanumeric:
    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore
'''

def alphanumeric(password):
    if password:
        for i in password:
                try:
                    try:
                        if int(i) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            pass
                        else:
                            return False
                    except:
                        if i.lower() in ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y","z"]:
                            pass
                        else:
                            return False
                except:
                    return False
        return True
    else:
        return False
# password = ""
password = "eGneuMgyg4RJgCTOlWI6qKX1AYv3b"
print(alphanumeric(password))

'''other solutions:
def alphanumeric(string):
    return string.isalnum()
==============
# An obvious, elegant solution is just to return string.isalnum()
# But I feel like this kata is broken.  The description says something about a buggy regular expression.
# I don't know what regular expression it's referring to, but to try to solve this in the spirit of
# the kata, I'm going to use a regular expression.
import re
pattern = re.compile('^[0-9a-zA-Z]+$')
def alphanumeric(string):
  return pattern.match(string) is not None
'''