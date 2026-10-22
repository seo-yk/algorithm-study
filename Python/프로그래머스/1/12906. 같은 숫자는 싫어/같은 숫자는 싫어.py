from collections import deque
def solution(arr):
    
    """
    arr: 0~9, 중복 제거, 원래 순서 유지
    """
    
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]: 
            answer.append(arr[i])
    
    return answer