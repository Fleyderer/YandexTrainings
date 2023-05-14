def solution(seq):
    min_1 = max_3 = min(seq[0], seq[1], seq[2])
    max_1 = max(seq[0], seq[1], seq[2])
    min_2 = max_2 = seq[0] + seq[1] + seq[2] - max_1 - min_1
    for i in range(3, len(seq)):

        if seq[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = seq[i]
        elif seq[i] > max_2:
            max_3 = max_2
            max_2 = seq[i]
        elif seq[i] > max_3:
            max_3 = seq[i]

        if seq[i] < min_1:
            min_2 = min_1
            min_1 = seq[i]
        elif seq[i] < min_2:
            min_2 = seq[i]

    return (min_1, min_2, max_1) if min_1 * min_2 * max_1 > max_1 * max_2 * max_3 else (max_1, max_2, max_3)


print(*solution([int(x) for x in input().split()]))
