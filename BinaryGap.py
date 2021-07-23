def solution(n):
    binary_String =  str(bin(n).replace("0b", ""))
    current_gap = 0
    filter = False
    max_gap = 0
    for char_index in range(len(binary_String)):
        if(binary_String[char_index] == '1' and filter == False):
           filter = True
        if(binary_String[char_index] == '0' and filter == True):
            current_gap += 1
        if(binary_String[char_index] == '1' and current_gap > 0 and current_gap > max_gap):
            max_gap = current_gap
            current_gap = 0
    return max_gap
    
print(solution(600))