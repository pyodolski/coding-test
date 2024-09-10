def solution(n):
    answer = 0
    i = 1
    while i < n:
        if n / i == i:
            answer = 1
            return answer
        i += 1
        
    else:
        answer = 2
    return answer