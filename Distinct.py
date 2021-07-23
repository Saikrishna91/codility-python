def solution(A):
    A.sort()
    for j in range(len(A)):
        if A.count(A[j]) == 1:
            return A[j]

    
a = []
print(solution(a))
