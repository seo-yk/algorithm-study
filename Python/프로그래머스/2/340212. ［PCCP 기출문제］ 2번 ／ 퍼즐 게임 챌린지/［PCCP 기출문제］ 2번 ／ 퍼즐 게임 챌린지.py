def solution(diffs, times, limit):
    n = len(times)
    
    left = min(diffs)
    right = max(diffs)
    answer = 0
    
    while left <= right:
        level = (left + right) // 2
        spent = 0
        for i in range(n):
            diff = diffs[i]
            time_cur = times[i]
            if i == 0:
                time_prev = 0
            else:
                time_prev = times[i-1]
        
            if diff <= level:
                spent += time_cur
            else:
                spent += (diff - level) * (time_cur + time_prev) + time_cur
        
        if spent > limit:
            left = level + 1
        else:
            answer = level
            right = level - 1
            
    return answer