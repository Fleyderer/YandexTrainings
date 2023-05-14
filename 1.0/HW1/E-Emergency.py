from math import ceil


def possible_apart_cnt(floors_before, apart_num):
    start = ceil(apart_num / (floors_before + 1))
    result = []
    while ceil(apart_num / start) == floors_before + 1:
        result.append(start)
        start += 1
    return result


def entrance_and_floor(apart_num, apart_on_floor, floor_cnt):
    apart_in_entrance = apart_on_floor * floor_cnt
    if apart_on_floor < 1:
        return -1, -1
    entrance_new = ceil(apart_num / apart_in_entrance)
    floor_new = ceil((apart_num - apart_in_entrance * (entrance_new - 1)) / apart_on_floor)
    return entrance_new, floor_new


def solution(apart_new, floor_cnt, apart_old, entrance_old, floor_old):
    entrance_new = 0
    floor_new = 0
    floors_with_entrances = floor_cnt * (entrance_old - 1) + floor_old - 1
    if floor_old > floor_cnt:
        entrance_new = floor_new = -1
    elif floors_with_entrances == 0:
        if apart_new == apart_old:
            floor_new = floor_old
            entrance_new = entrance_old
        elif apart_new < apart_old:
            floor_new = 1
            entrance_new = 1
        elif floor_cnt == 1:
            floor_new = 1
        elif apart_new <= apart_old * floor_cnt:
            entrance_new = 1
    else:
        possible_apart_on_floor = possible_apart_cnt(floors_with_entrances, apart_old)
        if len(possible_apart_on_floor) == 0:
            entrance_new = floor_new = -1
        else:
            possible_entrances, possible_floors = list(zip(*[entrance_and_floor(apart_new, apart_cnt, floor_cnt)
                                                             for apart_cnt in possible_apart_on_floor]))
            entrance_new = possible_entrances[0] if all(x == possible_entrances[0] for x in possible_entrances) else 0
            floor_new = possible_floors[0] if all(x == possible_floors[0] for x in possible_floors) else 0

    return entrance_new, floor_new


print(*solution(*map(int, input().split())))
