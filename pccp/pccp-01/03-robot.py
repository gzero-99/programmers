
def solution(board, k):
    # move
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # robot current location
    x, y, point = 0, 0, 1
    n = len(board)
    # stop when k sec
    while k > 0:
        # after 1sec (nx, ny)
        nx, ny = x + dx[point], y + dy[point]
        k -= 1
        # if meets end of map or a obstacle
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
            # flip 90 degree
            point = (point + 1) % 4
            continue
        x, y = nx, ny

    loc = [x, y]
    return loc

board = [[0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0]]

board2 = [[0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [1, 1, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]
k = 10
k2 = 20
print(solution(board2, k2))

