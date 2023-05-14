def solution(start, tracing):
    lt = 30
    rt = 4000
    prev_freq = start
    for freq, conclusion in tracing:
        nt = abs(freq - prev_freq) / 2
        if conclusion == "further":
            if freq > prev_freq:
                rt = min(rt, prev_freq + nt)
            else:
                lt = max(lt, freq + nt)
        else:
            if freq > prev_freq:
                lt = max(lt, prev_freq + nt)
            else:
                rt = min(rt, freq + nt)
        prev_freq = freq
    return lt, rt


n = int(input())
print(*solution(float(input()), [(c := input().split()) and (float(c[0]), c[1]) for _ in range(n - 1)]))
