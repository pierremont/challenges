'''
Sort the odd
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''

def sort_array(source_array):
    my_dict = {}
    for i in range(len(source_array)):
        if source_array[i]%2 == 0:
            pass
        else:
            my_dict[i] = source_array[i]    #create a dictionary with the odd values and their position
    # print(my_dict)

    sorted_values = list(sorted(my_dict.values()))  #add the sorted values to a list
    sorted_keys = list(sorted(my_dict.keys())) #add the sorted keys to a list

    # check print
    for i in range(len(sorted_keys)):
        # print(i)
        # print("cheie =", sorted_keys[i], "valoare = ", sorted_values[i])
        source_array[sorted_keys[i]] = sorted_values[i]

    return source_array

# source_array = [5, 8, 6, 3, 4]
source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(source_array))

# test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
# test.assert_equals(sort_array([]),[])

'''
better solutions:
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
  
  
  def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
'''