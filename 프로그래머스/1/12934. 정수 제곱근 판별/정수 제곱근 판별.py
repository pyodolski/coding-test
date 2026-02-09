import math

def integer_square_root(n):
    sqrt_result = math.sqrt(n)
    return int(sqrt_result)

def solution(n):
    sqrt_n = math.sqrt(n)
    answer = 0
    if sqrt_n.is_integer():
        answer = integer_square_root(n)
        answer = (answer + 1) * (answer + 1)
        return answer
    else:
        return -1

        