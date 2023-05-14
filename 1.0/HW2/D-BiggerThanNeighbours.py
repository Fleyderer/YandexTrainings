def solution(seq):
    cnt = 0
    for i in range(1, len(seq) - 1):
        cnt += seq[i] > seq[i - 1] and seq[i] > seq[i + 1]
    return cnt


print(solution([int(x) for x in input().split()]))
