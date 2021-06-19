"""quick sort easy way with increased space complexity"""
# def quick_sort(arr):
#     length = len(arr)
#     if length <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#         items_greater = []
#         items_smaller = []
#
#         for each in arr:
#             if each > pivot:
#                 items_greater.append(each)
#             else:
#                 items_smaller.append(each)
#         return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)
#
# arr = [5,5,6,7,9,1,22,4,67,8,9,0]
# print(quick_sort(arr))

# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end
#
#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and array[high] >= pivot:
#             high = high - 1
#
#         # Opposite process of the one above
#         while low <= high and array[low] <= pivot:
#             low = low + 1
#
#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break
#
#     array[start], array[high] = array[high], array[start]
#
#     return high
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     p = partition(array, start, end)
#     quick_sort(array, start, p-1)
#     quick_sort(array, p+1, end)
#
# array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
#
# quick_sort(array, 0, len(array) - 1)
# print(array)


def quick_sort(A):
    quick_sort_2(A, 0, len(A)-1)

def quick_sort_2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort_2(A, low, p-1)
        quick_sort_2(A, p+1, high)

def partition(A, low, high):
    p_i  = get_pivot(A, low, high)
    p_v = A[p_i]
    A[p_i], A[low] = A[low], A[p_i]
    border = low

    for i in range(low,high+1):
        if A[i] < p_v:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]
    return border

def get_pivot(A, low, high):
    mid = (low + high)//2
    pivot = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
        elif A[low] > A[high]:
            pivot = low

    return pivot

arr = [17,41,5,22,54,6,29,3,13]
quick_sort(arr)
print(arr)
