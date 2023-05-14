def solution(seq):
    return "YES" if all(seq[i] < seq[i + 1] for i in range(len(seq) - 1)) else "NO"


print(solution(list(map(int, input().split()))))
