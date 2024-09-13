def solution(mats, park):
    # 돗자리 크기 으로 큰 것부터 정렬
    mats.sort(reverse=True)
    
    n = len(park)  # 행 
    m = len(park[0])  # 열
    
    
    def check_place(i, j, size):
        if i + size > n or j + size > m:
            return False
        for x in range(i, i + size):
            for y in range(j, j + size):
                if park[x][y] != "-1": # size 만큼 옮기면서 -1 확인
                    return False
        return True
    
    for size in mats:
        for i in range(n):
            for j in range(m):
                if check_place(i, j, size):
                    return size
    return -1