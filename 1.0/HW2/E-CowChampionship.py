def solution(competitors):
    win_idx = 0
    search_idx = 0
    for i in range(1, len(competitors)):

        if competitors[i] % 10 == 5:
            if i + 1 < len(competitors) and competitors[i] > competitors[i + 1]:
                if search_idx == 0 or competitors[i] > competitors[search_idx]:
                    search_idx = i

        if competitors[i] > competitors[win_idx]:
            win_idx = i
            search_idx = 0

    if search_idx == 0:
        return 0

    place = 1
    for i in range(len(competitors)):
        place += competitors[i] > competitors[search_idx]
    return place


_ = int(input())
print(solution([int(x) for x in input().split()]))
