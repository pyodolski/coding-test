def solution(n):
    start = n + 1
    while start > n:
        cnt = bin(start).count('1')
        if cnt == bin(n).count('1'):
            break
        else:
            start += 1
    return start