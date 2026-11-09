def solution(array, commands):
    answer = []
    
    for com in commands:
        if len(com) >= 3:
            i = com[0]-1
            j = com[1]
            k = com[2]-1
            
            temp = sorted(array[i:j])
            answer.append(temp[k])
    
    return answer