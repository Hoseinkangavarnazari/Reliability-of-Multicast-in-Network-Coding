# Implementation of calulation of Reibility of Multicast Under random linear network coding
# Evengy Tsimbalo & Andrea Tassi
# coded by Hosein Kangavar Nazari
import numpy as np
import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom



# q denotes Finite field size , m received packet in decoding matrix, K is number of symbols to decode
def full_rank_probability(q, m, k):
    if m < k:
        return 0
    answer = 1
    for i in range(k):
        answer *= 1 - pow(q, i-m)
    return answer


def i_rank_probability(q, mu, k, i):
    preEquation = 1 / pow(q, (mu - i)*(k-i))
    answer = preEquation
    for l in range(i):
        numeratorLeft = 1 - pow(q, l - mu)
        numeratorRight = 1 - pow(q, l - k)
        denominator = 1 - pow(q, l-i)
        answer *= (numeratorLeft*numeratorRight)/denominator
    return answer


if __name__ == "__main__":
    test = full_rank_probability(2, 15, 10)
    print(ncr(5,3))
