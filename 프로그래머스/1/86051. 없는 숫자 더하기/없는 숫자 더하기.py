def solution(numbers):
    answer = 0
    num = [0,1,2,3,4,5,6,7,8,9]
    i = 0
    while i < len(numbers):
        if numbers[i] in num:
            answer += numbers[i]
            i += 1
        else:
            i += 1
    return 45 - answer