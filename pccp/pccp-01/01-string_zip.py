# 문자열 탐색하면서 해싱, 시뮬레이션
# ex. 로봇 격자 이동, 구현이 1번 문제
import sys


def solution(s):
    answer = ""
    before = ""
    count = 0
    for c in s:
        if before == c:
            count += 1
        else:
            answer += before + (str(count) if count > 1 else "")
            before = c
            count = 1
    answer += before + (str(count) if count > 1 else "")

    return answer

s = sys.argv[1]
print(solution(s))

# 해싱해서 풀면 안되는 문제 임, H가 1개인 경우 표시되면 안됨.
# 앞에서부터 선형 탐색해가면서 풀기
