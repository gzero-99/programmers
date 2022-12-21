import sys


def solution(s):
    book = dict()
    b_max = 0
    result = ""
    for i in s:
        if i not in book.keys():
            book[i] = 1
        else:
            book[i] += 1
        if b_max < book[i]:
            b_max = book[i]
            result = i
    return result


s = sys.argv[1]
print(solution(s))

import sys


def solution_soso(s):
    count = dict()

    for c in s:
        if c not in count.keys():
            count[c] = 1
        else:
            count[c] += 1

    return max(count, key=count.get)


string = sys.argv[1]
print(solution_soso(string))