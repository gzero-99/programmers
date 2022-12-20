import  sys

def solution(s):
    answer = ""
    prev = None
    cnt = 0
    for cur in s:
        if prev != cur and prev is not None:
            answer += prev
            if cnt > 1:
                answer += str(cnt)
            cnt = 1
        else:
            cnt += 1
        prev = cur
    answer += prev
    if cnt > 1:
        answer += str(cnt)

    return answer

s = sys.argv[1]
print(solution(s))