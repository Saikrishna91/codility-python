def solution(A):
    if len(A) == 0:
        return -1

    d_key = 0
    d_value = 0

    unique = set(A)
    for i in unique:
        if A.count(i) > d_value:
            d_key = i
            d_value = A.count(i)

    if d_value < len(unique):
        return -1    
    
    return A.index(d_key)

myList = [3, 1, 1, 4]
print(solution(myList))