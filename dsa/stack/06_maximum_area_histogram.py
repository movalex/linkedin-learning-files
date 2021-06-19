from stack import Stack

"""
given a histogram with height of each tower given as input list
find the maximum area of rectangle than can be formed joining one or more histogram tower
"""

def find_left(arr, n):
    result = []
    s = Stack()
    psudo_index = -1

    for i in range(n):

        if s.is_empty():
            result.append(psudo_index)

        elif (s.is_empty() == False and s.peek()[0] < arr[i]):
            result.append(s.peek()[1])

        elif (s.is_empty() == False and s.peek()[0] >= arr[i]):
            while (s.is_empty() == False and s.peek()[0] >= arr[i]):
                s.pop()

            if s.is_empty():
                result.append(psudo_index)

            else:
                result.append(s.peek()[1])

        s.push((arr[i],i))

    print(result)
    return result


def find_right(arr, n):
    result = []
    s = Stack()
    psudo_index = n

    for i in range(n)[::-1]:

        if s.is_empty():
            result.append(psudo_index)

        elif (s.is_empty() == False and s.peek()[0] < arr[i]):
            result.append(s.peek()[1])

        elif (s.is_empty() == False and s.peek()[0] >= arr[i]):
            while (s.is_empty() == False and s.peek()[0] >= arr[i]):
                s.pop()

            if s.is_empty():
                result.append(psudo_index)

            else:
                result.append(s.peek()[1])

        s.push((arr[i],i))

    print(list(reversed(result)))
    return list(reversed(result))


if __name__ == '__main__':
    arr = [6,2,5,4,5,1,6]
    n = len(arr)
    left = find_left(arr, n)
    right = find_right(arr, n)
    max_area = 0
    for i,j,k in zip(left,right,arr):
        area = ((j - i) - 1)*k
        if area > max_area:
            max_area = area
    print(max_area)