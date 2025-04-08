def solution(num):
    answer = 0
    count = 0

    while num != 1:
        if num % 2 == 0:
            num /=  2
            count += 1
            if count == 500:
                return -1
            
        elif num % 2 != 0:
            num *= 3
            num += 1
            count +=  1
            if count == 500:
                return -1
    if num == 1 and count < 500:
        return count
 