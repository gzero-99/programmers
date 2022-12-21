from collections import Counter
import sys


def solution(s):
    answer = ""
    sH = Counter(s)
    # print(sH)
    s_max = 0

    for [key, val] in sH.items():
        # print(key, val)
        if s_max < val:
            s_max = val
            answer = key

    return answer


s = sys.argv[1]
print(solution(s))