def solution(seq, num):
    cl_id = 0
    for i in range(1, len(seq)):
        if abs(num - seq[i]) < abs(num - seq[cl_id]):
            cl_id = i
    return seq[cl_id]


_ = int(input())
print(solution([int(x) for x in input().split()], int(input())))
