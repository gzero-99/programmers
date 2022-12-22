from collections import defaultdict


def solution(input_string):
    answer = ""
    sH = defaultdict(int)
    prev = None
    for cur in input_string:
        if prev != cur:
            sH[cur] += 1
        prev = cur
    print(sH)
    flag = 0

    for key in sH:
        if sH[key] >= 2:
            answer += key
            flag = 1
    if flag == 0:
        answer = "N"

    return "".join(sorted(answer))

"""
test code 
"""
from collections import defaultdict


def dict_exercise(s):
    sH = defaultdict(set)
    for x in s:
        a, b = x.split(" ")
        sH[a].add(b)

    for key in sH:
        print(key)
        for x in sH[key]:
            print(key, x)


print(solution(["tom john", "tom luis", "park kim"]))