''' Who is the killer? Some people have been killed!

You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.
Task.
Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:
{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}

and also a list of the names of the dead people:
['Lucas', 'Bill']

return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'''


def who_killer(suspect_info, dead):
    for i, j in suspect_info.items():
        count = 0
        for x in dead:
            if x in j:
                count += 1
                if count == len(dead):
                    return i



suspect_info = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}
dead = ['Lucas', 'Bill']
# suspect_info = {'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}
# dead = ['Ben']
print(who_killer(suspect_info, dead))

''' other solutions:
def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name
            
            
def killer(suspect_info, dead):
    for x in suspect_info:
        if all(people in suspect_info[x] for people in dead):
            return x

'''
