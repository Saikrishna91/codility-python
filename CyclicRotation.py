def solution(A, K):
    rotatedArray = [None] * len(A)
    for i in range(len(A)):
        rotatedIndex = (i + K) % len(A)
        rotatedArray[rotatedIndex] = A[i]

    return rotatedArray
mylist = [1, 2, 3]
print(solution(mylist, 2))