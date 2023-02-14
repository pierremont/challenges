from collections import Counter

def even(word):
    count = Counter(word)
    letter_cut = 0
    for key, value in count.items():
        print(key, value)
        if value % 2 == 0 :
            print ('key ', key, ' is even')
        else:
            print ('key ', key, ' is not even')
            letter_cut += 1
    return letter_cut

x = even('aabrrggg')
print(x)
