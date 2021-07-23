def solution(A):
    A.sort()
    count = 0
    if len(A) < 2:
        return 0
    if len(A) == 2:
        return (A[0] + A[1]) // 2

    for i in range(len(A)):
        count += A[i]
    
    total_avg = count // len(A)
    print(total_avg)
    start_avg = (A[0] + A[1]) // 2
    print(start_avg)
    if total_avg < start_avg:
        return total_avg
    else:
        return start_avg

myList = [5, 6, 3, 4, 9]
print(solution(myList))