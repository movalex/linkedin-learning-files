"""
default binary search (recursive)
"""
# def binary_search(arr, low, high, x):
#
#     while low <= high:
#
#         mid = (low + high)//2
#
#         if arr[mid] == x:
#             return mid
#         if arr[mid] > x:
#             return binary_search(arr, low, mid-1, x)
#         if arr[mid] < x:
#             return binary_search(arr, mid+1, high, x)
#
#     return - 1

# arr = [1,2,3,4,5,5,6,7,7,8,9,10]
# x = 7
# print(binary_search(arr, len(arr)-1, 0, 1))

"""
default binary search (iterative)
"""
# def binary_search_iterative(arr,x):
#
#     high = len(arr)-1
#     low = 0
#     result = -1
#
#     while high>low:
#
#         mid = (high + low) // 2
#
#         if x == arr[mid]:
#             result = mid
#             break;
#         elif x > arr[mid]:
#             low = mid
#         elif x < arr[mid]:
#             high = mid
#
#     return result

# arr = [1,2,3,3,4,5,5,6,7,7,8,9,10]
# x = 7
#
# print(binary_search_iterative(arr,1))

"""
implement binary seach to find index of number in an infinite array
"""

def binary_search(arr, low, high, x):

    if low <= high:

        mid = (low + high)//2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        if arr[mid] < x:
            return binary_search(arr, mid+1, high, x)

    return - 1

def binary_find_infinite(arr, x):

    low = 0
    high = 1
    val = arr[1]

    while x > val:
        low = high
        high = high * 2
        val = arr[high]

    print(binary_search(arr, low, high, x))

arr = [1,2,3,4,5,6,7,8,9,10]
x = 1

binary_find_infinite(arr,x)


[12,15,2,5,6,8,11]