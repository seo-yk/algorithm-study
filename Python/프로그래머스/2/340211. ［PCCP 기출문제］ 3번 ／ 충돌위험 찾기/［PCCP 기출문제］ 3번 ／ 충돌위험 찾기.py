from collections import defaultdict, Counter

def solution(points, routes):
    pm = {}
    for i, (r, c) in enumerate(points):
        pm[i+1] = (r, c)
        
    time = defaultdict(list)
    for route in routes:
        t = 0
        # 시작 좌표
        cur_r, cur_c = pm[route[0]]
        time[t].append((cur_r, cur_c))
    
        for i in range(1, len(route)):
            next_r, next_c = pm[route[i]]
            
            while cur_r != next_r:
                if cur_r < next_r:
                    cur_r += 1
                else:
                    cur_r -= 1
                t += 1
                time[t].append((cur_r, cur_c))
                
            while cur_c != next_c:
                if cur_c < next_c:
                    cur_c += 1
                else:
                    cur_c -= 1
                t += 1
                time[t].append((cur_r, cur_c))
    
    total = 0
    for key, value in time.items():
        positions = Counter(value)
        for k, v in positions.items():
            if v >= 2:
                total += 1
            
    return total
