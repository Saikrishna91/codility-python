def solution(A):
    A.sort()
    if len(A) < 3:
        return 0

    if len(A) >= 3:
        prefix_count = A[0] * A[1] * A[2]
        prefix_count_1 = A[0] * A[1] * A[len(A) - 1]
        suffix_count = A[len(A) - 3] * A[len(A) - 2] * A[len(A) - 1]
        suffix_count_1 = A[0] * A[len(A) - 2] * A[len(A) - 1]

    max_count_1 = max(prefix_count, prefix_count_1)
    max_count_2 = max(suffix_count, suffix_count_1)

    return max(max_count_1, max_count_2)
    
myList = [-5, 5, -5, 4]
print(solution(myList))