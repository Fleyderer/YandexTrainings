def solution(seq):
    min_1 = max_2 = min(seq[0], seq[1])
    max_1 = min_2 = max(seq[0], seq[1])
    for i in range(2, len(seq)):

        if seq[i] > max_1:
            max_2 = max_1
            max_1 = seq[i]
        elif seq[i] > max_2:
            max_2 = seq[i]

        if seq[i] < min_1:
            min_2 = min_1
            min_1 = seq[i]
        elif seq[i] < min_2:
            min_2 = seq[i]

    return (min_1, min_2) if min_1 * min_2 > max_1 * max_2 else (max_2, max_1)


print(*solution([int(x) for x in input().split()]))
