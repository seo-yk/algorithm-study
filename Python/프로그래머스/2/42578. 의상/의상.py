def solution(clothes):
    cd = {}
    
    for c in clothes:
        cd[c[1]] = cd.get(c[1], 0) + 1
    
    cnt = 1
    for x, y in cd.items():
        cnt = cnt * (y + 1)
        
    return cnt-1