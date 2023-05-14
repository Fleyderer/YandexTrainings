now, then = map(int, input().split())
option = input()

match option:
    case "heat":
        result = max(now, then)
    case "freeze":
        result = min(now, then)
    case "auto":
        result = then
    case "fan":
        result = now
    case _:
        result = None

print(result)