from collections import Counter

def solution(nums):
    n = len(nums) // 2
    pd = Counter(nums)
    
    if n < len(pd):
        return n
    else:
        return len(pd)