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

x, y = 1, 1

queue = [[1, 1, 0]]
log = [[1, 1]]

while True:
    x, y, deepth = queue.pop(0)

    for move in d:
        dx = x + move[0]
        dy = y + move[1]

        if maze[dx][dy] == 1:
            print(f'The minmum deepth is: {deepth + 1}')
            exit(0)
        else:
            if maze[dx][dy] != 9:
                if [dx, dy] not in log:
                    log.append([dx, dy])
                    queue.append([dx, dy, deepth + 1])
