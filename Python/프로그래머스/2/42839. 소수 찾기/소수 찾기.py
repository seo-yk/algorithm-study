import math
def solution(numbers):
    
    num_len = len(numbers)
    
    ns = set()
    visited = [False] * num_len
    
    def dfs(path, length):
        if len(path) == length:
            cur = int(''.join(path[:]))
            if cur != 0:
                ns.add(cur)
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                path.append(numbers[i])
                dfs(path, length)
                path.pop()
                visited[i] = False
    
    for i in range(1, num_len+1):
        dfs([], i)
    
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    for num in ns:
        if isPrime(num):
            answer += 1
    
    return answer