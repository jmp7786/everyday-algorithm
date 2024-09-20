class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        m = len(board[0])
        grid = [-1] * (n * m)
        
        index = 0
        reverse = False  # flag to toggle reverse mode
        
        for i in range(n-1, -1, -1):  # 보드의 끝에서부터 위로 순회
            if reverse:
                # 행을 반대로 순회 (지그재그 패턴의 일부)
                for j in range(m-1, -1, -1):
                    grid[index] = board[i][j]
                    index += 1
            else:
                # 행을 그대로 순회
                for j in range(m):
                    grid[index] = board[i][j]
                    index += 1
            # 매 행마다 reverse를 토글
            reverse = not reverse
        
        # Flatten된 grid 확인
        print(grid)
        # 이후 DFS나 BFS 같은 탐색 방법으로 문제를 해결합니다.
        # BFS가 더 효율적이니 여기에 BFS를 적용하겠습니다.
        
        # BFS to find shortest path
        from collections import deque
        queue = deque([(0, 0)])  # 시작점과 이동 횟수
        visited = set([0])

        while queue:
            pos, moves = queue.popleft()

            # 마지막 셀에 도달하면 결과 반환
            if pos == len(grid) - 1:
                return moves

            # 다음 가능한 6칸 탐색
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos >= len(grid):
                    break
                
                # 사다리나 뱀이 있으면 그 위치로 이동
                if grid[next_pos] != -1:
                    next_pos = grid[next_pos] - 1

                # 방문한 적 없는 위치만 탐색
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1  # 만약 도달할 수 없는 경우