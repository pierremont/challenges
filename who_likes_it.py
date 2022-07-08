''' www.codewars.com
Who likes it?
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
'''


def likes(names):
    if len(people)==0:
        return "no one likes this"
    elif len(people)==1:
        return people[0] + " likes this"
    elif len(people)==2:
        return people[0] + " and " + people[1] + " like this"
    elif len(people)==3:
        return people[0] + ", " + people[1] + " and " + people[2] + " like this"
    elif len(people)==4:
        return people[0] + ", " + people[1] + " and " + str(len(people)-2) + "others like this"

def main(people):
    print(likes(names))

names = ["peter",'alex', 'marius', 'gina']
main(people)