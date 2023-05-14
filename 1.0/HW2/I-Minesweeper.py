def solution(n, m, mines):
    field = [[0 for _ in range(m)] for _ in range(n)]
    for mine in mines:
        field[mine[0] - 1][mine[1] - 1] = '*'

        for i in range(max(0, mine[0] - 2), min(mine[0] + 1, n)):
            for j in range(max(0, mine[1] - 2), min(mine[1] + 1, m)):
                if field[i][j] != '*':
                    field[i][j] += 1

    return field


n, m, k = [int(x) for x in input().split()]
mines = [[int(x) for x in input().split()] for _ in range(k)]
print('\n'.join([' '.join([str(x) for x in row]) for row in solution(n, m, mines)]))
