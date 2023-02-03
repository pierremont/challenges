
''' This is a demo task.
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.'''

def solution(A):
    N = len(A)
    my_list = list(range(N, 0, -1))
    print('my_list is', my_list)
    smallest = my_list[0]
    print('smallest = ', smallest)
    #for i in my_list[:0:-1]:
    for i in (my_list):
        print(i)
        if i not in A and i < smallest:
            smallest = i
    if smallest not in A:
        return smallest
    else:
        return len(A) + 1

#A = [1, 3, 6, 4, 1, 2]
A = [1, 2, 3]
print('final number is = ', solution(A))
