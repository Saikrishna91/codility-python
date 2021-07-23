def solution(S, P, Q):
    resultArray = [None] * len(P)
    for i in range(len(P)):
        resultArray[i] = findMatches(S, P[i], Q[i])
    return resultArray

def findMatches(S, element_P, element_Q):
    if 'A' in S[element_P : element_Q + 1]:
        return 1
    if 'C' in S[element_P : element_Q + 1]:
        return 2
    if 'G' in S[element_P : element_Q + 1]:
        return 3
    return 4


S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))