def solution(A):
    P = 1
    sum1 = A[0]
    sum2 = 0
    for i in range(len(A)):
        if i > P:
            sum2 += A[i]
    diff = sum1 - sum2 
    for i in range(len(A) - 1):
        if(i > P):
            sum1 += A[i]
            sum2 -= A[i]
        newDiff = abs(sum1 - sum2)
        if newDiff < diff:
           diff = newDiff
    return abs(diff)

myList = [3, 1, 2, 4, 3]
print(solution(myList))