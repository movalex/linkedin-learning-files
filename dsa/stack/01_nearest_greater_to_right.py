from stack import Stack

def find(arr,n):
    
    result = []
    s = Stack()
    
    for i in range(n)[::-1]:
        
        if s.is_empty():
            result.append(-1)
        elif (s.is_empty() ==  False and s.peek() > arr[i]):
            result.append(s.peek())
        elif (s.is_empty() == False and s.peek() <= arr[i]):
            while (s.is_empty() == False and s.peek() <= arr[i]):
                s.pop()
            if s.is_empty():
                result.append(-1)
            else:
                result.append(s.peek())
        s.push(arr[i])
    
    print(list(reversed(result)))
        
if __name__ == '__main__':
    
    arr = [1,3,2,4]
    n = len(arr)
    find(arr, n)
    
    

