def solution(a, b, c, d, e, f):
    delta = a * d - b * c
    delta_x = e * d - b * f
    delta_y = a * f - c * e
    if delta == 0:
        if a == b == c == d == e == f == 0:
            return [5]
        elif a == b == 0 and e != 0:
            return [0]
        elif c == d == 0 and f != 0:
            return [0]
        elif delta_x == 0:
            if a == c == 0:
                return 4, f / d if b == 0 else e / b
            elif b == d == 0:
                return (3, f / c if a == 0 else e / a) if delta_y == 0 else [0]
            else:
                return (1, - a / b, e / b) if d == 0 else (1, - c / d, f / d)
        else:
            return [0]
    else:
        return 2, delta_x / delta, delta_y / delta


print(*solution(*[float(input()) for _ in range(6)]))
