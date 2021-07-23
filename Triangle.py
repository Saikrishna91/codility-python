def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0


myList = [10, 2, 5, 1, 20]
print(solution(myList))