
def first_missing_positive(arr):
    """
    Given an unsorted integer array nums, find the smallest missing positive integer.
    Input: nums = [1,2,0]
    Output: 3

    Input: nums = [3,4,-1,1]
    Output: 2

    Input: nums = [7,8,9,11,12]
    Output: 1

    """
    n = len(arr)
    #base case
    if n == 0 or 1 not in arr:
        return 1
    # change every un-useful(lesser than 1 and greater than length of array) value to 1

    for i in range(n):
        if arr[i ]< 1 or arr[i]>n:
            arr[i] = 1

    # mark the values to -1*x
    for i in range(n):
        indx = abs(arr[i]) -1
        if arr[indx] > 0:
            arr[indx] = - 1 * arr[indx]

    for i, num in enumerate(arr):
        if num > 0:
            return i+1

    return n + 1


print(first_missing_positive([3, 4, -1, 1]))


def maximum_Subarray(arr):
    """
    Given an integer array nums,
    find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    """
    bestArray = bestSum = arr[0]
    for num in arr[1:]:
        bestArray = max(num, bestArray+num )
        bestSum = max(bestArray,bestSum)
    return bestSum



print(maximum_Subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
