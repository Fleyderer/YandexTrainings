n, k, m = map(int, input().split())

m_cnt = 0

while n >= k:
    k_cnt, n = divmod(n, k)
    if k_cnt:
        cnt, res = divmod(k, m)
        if cnt:
            m_cnt += cnt * k_cnt
            n += res * k_cnt

print(m_cnt)
