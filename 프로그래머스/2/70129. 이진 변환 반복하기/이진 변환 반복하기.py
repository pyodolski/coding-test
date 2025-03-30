def solution(s):
    cnt = 0
    i = 0
    while s != '1':
        cnt += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]     # 이진수 변환
        i += 1
    return [i, cnt]