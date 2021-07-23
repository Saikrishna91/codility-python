def solution(A, B, K):
    count = 0
    if A == B:
        return 0
    for i in range(A, B):
        if i % K == 0:
            count += 1
    return count

print(solution(0, 1, 11))