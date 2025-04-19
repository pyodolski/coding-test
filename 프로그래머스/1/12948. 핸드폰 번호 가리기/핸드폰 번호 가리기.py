def solution(phone_number):
    i = 0
    answer = ''
    len1 = len(phone_number) - 4
    while i < len1:
        answer += '*'
        i += 1
    while i < len(phone_number):
        answer += phone_number[i]
        i += 1
    return answer