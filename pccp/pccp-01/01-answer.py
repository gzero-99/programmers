import sys


def solution(s):
    answer = ""
    prev = None
    cnt = 0
    for cur in s:
        if prev != cur and prev is not None:  # 앞 뒤 둘이 다르다
            answer += prev
            if cnt > 1:
                answer += str(cnt)
            cnt = 1
        else:  # 앞 뒤 둘이 같다
            cnt += 1
        prev = cur

    answer += prev
    if cnt > 1:
        answer += str(cnt)

    return answer


s = sys.argv[1]
print(solution(s))
