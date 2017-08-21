# author : Mohammed Rashid Chowdhury
# This is an python implementation of mergesort.
# the psceducode was taken from introduction to algorithm by cormens book.

import sys,math

def merge(A,p,q,r):

    n1 = q-p+1
    n2 = r-q
    # for storing the values of the array A in two temporary arrays.
    L= []
    R= []

    for i in range(0,n1):
        L.append(A[p+i])

    for j in range(0,n2):
        R.append(A[q+j+1])
    '''
    The following two lines set the last element of the arrays as a max number the system can provide (infinite).
    this is called sentinels in cormens book and they are used to make sure the array has reached at end.
    When sentinels are reached values from other array are copied into main array. if they are not used wrong values can append into main array.
    For example if the last element of left array is 23 and the right array is not yet finished traversing then the remaining elements of right array will be compared to 23.
    Which is wrong.
    '''
    L.append(sys.maxsize)
    R.append(sys.maxsize)

    i = 0
    j = 0

    for k in range(p,r+1):

        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1

        else:
            A[k] = R[j]
            j+=1

    return A

def merge_sort(A,p,r):

    if (p<r):

        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A, q+1, r)
        merge(A,p,q,r)

if __name__ == "__main__":
    inputArray= list(map(int, input().strip().split(' ')))
    merge_sort(inputArray,0,len(inputArray)-1)
    print(inputArray)

