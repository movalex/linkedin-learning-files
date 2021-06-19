# Write a program to find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum
#         int [] a = {-2, -3, 4, -1, -2, 1, 5, -3};


# def find_sum(arr):
#
#     max_sum = 0
#     new_max = 0
#
#     for each in arr:
#
#         max_sum = max_sum + each
#
#         max_sum = max(max_sum, 0)
#
#         new_max = max(new_max, max_sum)
#
#     return new_max
#
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# res = find_sum(arr)
# print(res)

# 1 --- 2 --- 3---4
#             5----6


def detect_loop(linked_list):

    if linked_list.head is None:
        return 0

    low = linked_list.head
    high = linked_list.head
    count = 1

    while(low and high and low.next and high.next.next):

        if low == high and count != 1:

            while(low != high):
                low = low.next
                count = count + 1
            return count

        low = low.next
        high = high.next.next

    return 0




