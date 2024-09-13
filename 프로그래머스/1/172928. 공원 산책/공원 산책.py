def solution(park, routes):

    x, y = 0, 0 
    w, h = len(park[0]), len(park)
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    # S 검색
    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":
                x, y = i, j
                break 
                
     # 명령어 파싱   
    for r in routes:
        d, n = r.split(" ")
        dx, dy = x, y
        
        for i in range(int(n)):
            
            nx = x + op[d][0]
            ny = y + op[d][1]
        
            if 0 <= nx <= h-1 and 0<= ny <= w-1 and (park[nx][ny]!="X"):
                # 직사각형 내부에 들어있는지 검사, 장애물인지 검사
                x, y = nx, ny
                    
            else:
                x, y = dx, dy
                break

    return (x,y)