"""
Given an array A[] and a number x, check for pair in A[] with sum as x
"""
# def two_sum_hashtable(arr, target):
#     ht = dict()
#     for i in range(len(arr)):
#         if arr[i] in ht:
#             print(arr[i], ht[arr[i]])
#         else:
#             ht[target - arr[i]] = arr[i]


# two_sum_hashtable([2,6,4,8], 10)


# def two_sum_brute_force(arr, target):
#     for each in arr:
#         diff = target - each
#         if diff in arr:
#             print(each, diff)
#
# two_sum_brute_force([2,4,6,8,10,-2], 10)

def two_sum(arr, target):

    low = 0
    high = len(arr)-1

    while low <= high:
        if arr[low] + arr[high] == target:
            print(arr[low], arr[high])
            low = low + 1
        elif arr[low] + arr[high] > target:
            high = high - 1
        elif arr[low] + arr[high] < target:
            low = low +1

two_sum([-2,0,2,4,6,8,10,12], 10)