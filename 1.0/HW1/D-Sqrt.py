a, b, c = [int(input()) for _ in range(3)]
if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if b == c ** 2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    print(int(r) if (r := (c ** 2 - b) / a) % 1 < 1e-7 else "NO SOLUTION")
