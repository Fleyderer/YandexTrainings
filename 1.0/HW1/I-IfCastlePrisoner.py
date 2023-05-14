a, b, c, d, e = [int(input()) for _ in range(5)]
print("YES" if a + b + c - max(a, b, c) - (mn := min(a, b, c)) <= max(d, e) and mn <= min(d, e) else "NO")
