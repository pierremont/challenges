''' I love you, a little , a lot, passionately ... not at all (codewars)
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
    "I love you"
    "a little"
    "a lot"
    "passionately"
    "madly"
    "not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.'''

def how_much_i_love_you(nb_petals):
    love_list = ["I love you",     "a little",     "a lot",     "passionately",     "madly",     "not at all"]
    if 0 < nb_petals < 7:
        return love_list[nb_petals-1]
    else:
        result = nb_petals % 6
        return love_list[result - 1 ]

print(how_much_i_love_you(15))

'''other solutions:
def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1] #g'''

'''def how_much_i_love_you(nb_petals):
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]'''