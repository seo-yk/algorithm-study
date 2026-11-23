def solution(n, times):
    
    left = 1
    right = (max(times) * n)
    answer = []
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            
        if cnt >= n:
            right = mid-1
            answer.append(mid)
        elif cnt < n:
            left = mid+1
            
    return min(answer)
            