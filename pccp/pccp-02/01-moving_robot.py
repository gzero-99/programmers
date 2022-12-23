def solution(command):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y, point = 0, 0, 1
    for c in command:
        if c == 'R':
            point = (point + 1) % 4
            continue
        elif c == 'L':
            point = (point - 1) % 4
            continue
        elif c == 'G':
            nx, ny = x + dx[point], y + dy[point]
        else:
            nx, ny = x - dx[point], y - dy[point]
        x, y = nx, ny
    answer = [x, y]
    return answer

