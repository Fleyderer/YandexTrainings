def solution(a, b, n, m):
    f, s, f_cnt, s_cnt = (a, b, n, m) if a < b else (b, a, m, n)

    f_min, s_min = f_cnt + f * (f_cnt - 1), s_cnt + s * (s_cnt - 1)
    f_max, s_max = f_cnt + f * (f_cnt + 1), s_cnt + s * (s_cnt + 1)
    if s_min - f_min > f or f_min > s_max:
        return [-1]
    else:
        min_time = max(f_min, s_min)
        max_time = min(f_max, s_max)
        return min_time, max_time


print(*solution(*[int(input()) for _ in range(4)]))
