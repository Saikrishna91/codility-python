def solution(A):
  A.sort()
  for index in range(0,len(A),2):
        boundary = len(A)-2
        if index <boundary:
            if A[index] != A[index+1]:
                return A[index]
        else:
            return A[-1]

a = [5,6,2,9,2,3,6,7,3,1,7,9,1]
print(solution(a))
