from collections import deque, defaultdict
def solution(land):
    """
     뽑을 수 있는 석유 최대량
     1개의 열만 관통할 수 있음
     
     1) 매장된 석유가 얼마나 있는가
     - 1 연결된 집합 너비 구하기
     2) 각 열마다 얼마의 석유를 뽑을 수 있는가
    """
    N = len(land)
    M = len(land[0])
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    visited = [[False for _ in range(M)] for _ in range(N)]
    area_map = defaultdict(list)
    
    for r in range(N):
        for c in range(M):
            col_arr = set()
            if land[r][c] == 1 and not visited[r][c]:
                q = deque([(r, c)])
                visited[r][c] = True
                area = 1
                col_arr.add(c)

                while q:
                    cr, cc = q.popleft()
                    
                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]

                        if 0 <= nr < N and 0 <= nc < M:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                area += 1
                                q.append((nr, nc))
                                col_arr.add(nc)

                for col in col_arr:
                    area_map[col+1].append(area)
                    
    answer = 0
    for k, values in area_map.items():
        result = 0
        for value in values:
            result += value
        answer = max(answer, result)
        
    return answer