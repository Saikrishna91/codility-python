import math
def solution(A, B, K):
    sum_B = math.floor(B // K)
    sum_A = math.floor(A // K)
    count = sum_B - sum_A
    if(A % K == 0):
        count += 1
    return count
print(solution(10, 10, 20))