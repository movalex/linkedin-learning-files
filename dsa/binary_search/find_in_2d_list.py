
def search(arr,x,m,n):

    high_i = m - 1
    high_j = n -1
    low_i = 0
    low_j = 0

    while (low_i <= high_i and low_j <= high_j):

        if arr[high_i][high_j] == x:
            print(high_i,high_j)
            return 1

        elif arr[high_i][high_j] < x:
            if arr[high_i][low_j] < x:






if __name__=='__main__':
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]

    n = len(arr[0])
    m = len(arr)
    x = 12
    search(arr,x, m, n)