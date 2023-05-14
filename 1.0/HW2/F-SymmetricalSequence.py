def solution(seq):
    i, j = 0, len(seq) - 1
    idx = -1
    while i < j:
        if seq[i] == seq[j]:
            if idx == -1:
                idx = i
            i += 1
            j -= 1
        else:
            idx = -1
            if j == len(seq) - 1:
                i += 1
            else:
                j = len(seq) - 1

    return ([len(seq) - 1 if idx == -1 else idx], seq[idx - 1::-1]) if idx != 0 else [[idx]]


_ = int(input())
[print(*s) for s in solution([int(x) for x in input().split()])]

