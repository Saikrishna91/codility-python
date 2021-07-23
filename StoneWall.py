def solution(A):
    count = 1
    stack = []
    lowest = A[0]
    if len(A) == 1:
        return 1

    for i in range(len(A)):
        if A[i] > A[i - 1]:
            stack.append(A[i])
            count += 1
        if A[i] < lowest:
            while len(stack) > 0:
                stack.pop()
            
            stack.append(A[i])
            lowest = A[i]
            count += 1
        
        if A[i] < A[i-1] and A[i] > lowest:
                while len(stack) > 0 and stack[-1] > A[i]:
                    stack.pop();   
                
                if len(A) > 0 and stack[-1] < A[i]:
                    stack.append(A[i])
                    count += 1  
    
    return count

myList = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(myList))