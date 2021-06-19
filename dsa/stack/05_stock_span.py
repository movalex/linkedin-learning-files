from stack import Stack

def find(arr, n):
    """
    given input price of stocks of each day
    return number of days previous to the current day in which stock prices are less or equal to consecutivly
    including the day itself
    """
    result = []
    s = Stack()

    for i in range(n):

        if s.is_empty():
            result.append(1)

        elif (s.is_empty() == False and s.peek()[0] > arr[i]):
            result.append(i-(s.peek()[1]))

        elif (s.is_empty() == False and s.peek()[0] <= arr[i]):
            while (s.is_empty() == False and s.peek()[0] <= arr[i]):
                s.pop()

            if s.is_empty():
                result.append(1)

            else:
                result.append(i-(s.peek()[1]))

        s.push((arr[i],i))

    print(result)


if __name__ == '__main__':
    arr = [100,80,60,70,60,75,85]
    n = len(arr)
    find(arr, n)