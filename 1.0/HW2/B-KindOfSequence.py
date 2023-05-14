from collections import OrderedDict


def solution(seq):
    types = OrderedDict((key, True) for key in ["CONSTANT", "ASCENDING", "DESCENDING",
                                                "WEAKLY ASCENDING", "WEAKLY DESCENDING", "RANDOM"])
    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            types["ASCENDING"] = False
            types["DESCENDING"] = False
        else:
            types["CONSTANT"] = False
            if seq[i] < seq[i + 1]:
                types["DESCENDING"] = False
                types["WEAKLY DESCENDING"] = False
            else:
                types["ASCENDING"] = False
                types["WEAKLY ASCENDING"] = False
    return next(key for key, value in types.items() if value)


a = []
while (val := int(input())) != -2000000000:
    a.append(val)

print(solution(a))
