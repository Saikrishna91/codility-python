def solution(X, Y, D):
    jumps = (Y - X) / D
    if (Y - X) % D > 0:
        return int(jumps) + 1
    return int(jumps)

print(solution(10, 85, 30))