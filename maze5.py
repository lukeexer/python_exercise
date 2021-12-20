maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 9, 0, 9, 9],
    [9, 0, 9, 9, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 0, 9, 0, 9, 0, 1, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9],
    [9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9]
]

d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

log = [[1, 1]]

step = []

def find_min(pos, deepth):
    x, y = pos[0], pos[1]

    if maze[x][y] == 1:
        step.append(deepth)
        return deepth

    for move in d:
        xd = x + move[0]
        yd = y + move[1]

        if maze[xd][yd] != 9:
            if [xd, yd] not in log:
                log.append([xd, yd])
                find_min([xd, yd], deepth + 1)

    step.append(999999)
    return 999999


find_min([1, 1], 0)
print(log)
print(step)
print(f'The minimum step is: {min(step)}')
