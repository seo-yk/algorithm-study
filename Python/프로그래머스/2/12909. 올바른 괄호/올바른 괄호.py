from collections import deque

def solution(s):
    
    if s.startswith(')') and s.endswith('('):
        return False
    
    if len(s) % 2 != 0:
        return False
    
    sq = deque(s)
    cnt = 0
    while sq:
        
        cur = sq.popleft()
        
        if cnt < 0:
            print('무야호')
            return False
        
        if cur == '(':
            cnt += 1
        else:
            cnt -= 1
    
    return cnt == 0