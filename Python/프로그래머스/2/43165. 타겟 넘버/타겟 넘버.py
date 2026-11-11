def solution(numbers, target):
    answer = 0
    N = len(numbers)
    visited = [False] * N
    
    def dfs(sum, start):
        nonlocal answer
        if start == N:
            if sum == target:
                answer += 1
            return
        
        dfs(sum-numbers[start], start+1)
        dfs(sum+numbers[start], start+1)
        

            
    dfs(0, 0)
    return answer