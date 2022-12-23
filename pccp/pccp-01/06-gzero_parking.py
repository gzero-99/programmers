from collections import defaultdict
import math


def solution(fees, records):
    answer = []

    # time should be with minute unit
    inTime = [0] * 10000  # largest num is 9999
    isIn = [0] * 10000  # to check if still at parkinglot
    sumT = [0] * 10000  # the time how long car have been to cal the payment
    # hour x 60 + min

    for x in records:
        time, num, in_out = x.split(" ")
        hour, minu = time.split(":")
        if in_out == "IN":
            inTime[int(num)] = int(hour) * 60 + int(minu)
            isIn[int(num)] = 1
        else:
            sumT[int(num)] += int(hour) * 60 + int(minu) - inTime[int(num)]
            isIn[int(num)] = 0

    # check the one whos are not out
    for i in range(0, 10000):
        if isIn[i] == 1:
            sumT[i] += 1439 - inTime[i]

    # calc fee
    # fees[1] + max(math.ceil((sumT[num]-fees[0])/fees[2]), 0)*fees[3] = 14600
    # save fee result of cars in order
    for i in range(0, 10000):
        if sumT[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumT[i] - fees[0]) / fees[2]), 0) * fees[3])

    return answer