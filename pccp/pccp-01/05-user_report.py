from collections import defaultdict


def solution(id_list, report, k):
    result = []
    reportHash = defaultdict(set)  # for user who reported
    stoped = defaultdict(int)  # for counting to stop

    # id list
    # report set
    for x in report:
        a, b = x.split(" ")
        if b not in reportHash[a]:
            stoped[b] += 1
        reportHash[a].add(b)
    # count user only once

    # user stop when more than k
    for id in id_list:
        mail = 0
        for user in reportHash[id]:
            if stoped[user] >= k:
                mail += 1
        result.append(mail)

    return result