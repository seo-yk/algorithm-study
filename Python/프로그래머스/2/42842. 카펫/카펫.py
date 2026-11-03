from collections import Counter
def solution(brown, yellow):
    
    num = brown + yellow
    
    ns = set()
    for i in range(2, num):
        if num % i == 0:
            ns.add((num//i, i))
    
    for w, h in ns:
        if w >= 3 and h >= 3:
            m = [[False for _ in range(h)] for _ in range(w)]
            
            for i in range(w):
                for j in range(h):
                    m[0][j] = True
                    m[i][0] = True
                    m[w-1][j] = True
                    m[i][h-1] = True
                    
            br = sum(row.count(True) for row in m)
            yl = sum(row.count(False) for row in m)
            if br == brown and yl == yellow and w >= h:
                return [w, h]
            