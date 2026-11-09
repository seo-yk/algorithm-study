def solution(citations):
    
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        
        if citation <= i:
            return i
            
    return len(citations)
    
    