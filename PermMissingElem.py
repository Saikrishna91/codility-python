def solution(A):
    if len(A) == 0:
        return 1
    A.sort()
    count = 1
    for i in range(len(A)):
        if A[i] != count:
           return count
        
        if A[i] == count:
            count += 1
    return count

myList = [2]
print(solution(myList))