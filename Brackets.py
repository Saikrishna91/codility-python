def solution(S):
    A = []
    for i in range(len(S)):
        if S[i] == '{':
            A.append('}')
        if S[i] == '[':
            A.append(']')
        if S[i] == '(':
            A.append(')')

        if S[i] == '}' or S[i] == ']' or S[i] == ')':
            if len(A) == 0:
                return 0
            else:
                pop = A.pop()
                if S[i] != pop:
                    return 0
    

    if len(A) != 0:
        return 0
    else:
        return 1 
    
string = "())"
print(solution(string))