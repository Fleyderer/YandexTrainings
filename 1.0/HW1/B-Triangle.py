a, b, c = [int(input()) for _ in range(3)]
print("YES" if (m := max(a, b, c)) < a + b + c - m else "NO")
