first, second = (lst := list(map(int, input().split())))[:2], lst[2:]

eq = list(set(first).intersection(second))

if len(eq) == 2:
    ln = max(first)
    wd = min(first) * 2
elif len(eq) == 1:
    ln = eq[0]
    wd = first[not first.index(eq[0])] + second[not second.index(eq[0])]
else:
    ln = wd = 0
    min_square = 2000000
    for f in first:
        for s in second:
            square = (cln := (f + s)) * (cwd := max(first[not first.index(f)], second[not second.index(s)]))
            if square <= min_square:
                ln = cln
                wd = cwd
                min_square = square

print(ln, wd)
