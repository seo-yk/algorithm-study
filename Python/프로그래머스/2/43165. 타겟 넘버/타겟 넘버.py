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
        
        if not visited[start]:
            visited[start] = True
            dfs(sum-numbers[start], start+1)
            dfs(sum+numbers[start], start+1)
            visited[start] = False
            
    dfs(0, 0)
    return answer