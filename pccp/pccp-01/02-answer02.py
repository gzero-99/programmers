from collections import defaultdict
def solution(s):
    answer = ""
    sH = defaultdict(int)
    # 기본적으로 key의 value값이 0으로 초기화 되어 있음.
    # key 가 없어도 ㄱㅊ
    for x in s:
        sH[x] += 1
    largest = 0
    for key in sH:
        # print(sH[key])
        if sH[key] > largest:
            largest = sH[key]
    return answer