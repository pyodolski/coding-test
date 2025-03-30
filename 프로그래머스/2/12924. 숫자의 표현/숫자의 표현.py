def solution(n):
    cnt = 0
    start = 1
    
    while start <= n:
        total = 0
        num = start 
        
        while total < n:
            total += num
            num += 1
        
        if total == n:
            cnt += 1
        
        start += 1
            
    return cnt 