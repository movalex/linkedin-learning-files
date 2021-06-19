def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        return binary_search(arr, mid + 1, r, x)

    return -1


def findPos(a, key):
    l, h, val = 0, 1, arr[0]

    # Find h to do binary search
    while val < key:
        l = h  # store previous high
        h = 2 * h  # double high index
        val = arr[h]  # update new val

    # at this point we have updated low and high indices,
    # thus use binary search between them
    return binary_search(a, l, h, key)


arr = [1,2,3,4,5,6,7,8,9,10]
x = 5
ans = findPos(arr,x)
if ans == -1:
    print("Element not found")
else:
    print("Element found at index",ans)