from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
        
        visited[i] = True
        q = deque([i])
        
        while q:
            cur = q.popleft()
            
            for next in range(n):
                if not visited[next] and computers[cur][next] == 1:
                    visited[next] = True
                    q.append(next)
                        
    return answer