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

# The probability of having rank i by Mu,k matrix
# for mutual packets


def i_rank_probability(q, mu, k, i):
    preEquation = 1 / pow(q, (mu - i)*(k-i))
    answer = preEquation
    for l in range(i):
        numeratorLeft = 1 - pow(q, l - mu)
        numeratorRight = 1 - pow(q, l - k)
        denominator = 1 - pow(q, l-i)
        answer *= (numeratorLeft*numeratorRight)/denominator
    return answer


# m  an array of pocket received by each receiver, N total packet sent, e an array of error between each link
def phi(m, N, e):
    answer = 1
    for i in range(0, len(m)):
        answer *= pow((1 - e[i]), m[i]) * pow(e[i], N-m[i])
    return


def beta(m, mu, N, L):
    answer = 0
    z = min(m) - mu
    for l in range(0, z + 1):
        tempOuter = 1
        sign = pow(-1, l)
        comb = ncr(N-mu, l)

        tempInner = 1
        for j in range(L):
            tempInner *= ncr(N-mu-1, m[j]-mu-1)
        tempOuter = sign * comb * tempInner
        answer += tempOuter

    return answer


def everyPossibleSet(N, L):
    result = []
    buckets = [0] * L
    temp = buckets[:]
    result.append(temp)
    for i in range(0, L):
        i = 0
        for j in range(0, N+1):
            buckets[i] += 1
            temp = buckets[:] 
            result.append(temp)
        # search for another element which is not N
        for k in range(i, L):
            if(buckets[k] < N):
                buckets[k] += 1
                for ii in range(0, k):
                    buckets[ii] = 0
                result.append(buckets)
                break
    return result   
            
    return result


if __name__ == "__main__":
    test = full_rank_probability(2, 15, 10)
    print(ncr(5, 3))
    a = everyPossibleSet(2, 4)
    arr = [3, 2, 1, 2, 3, 12]
    mina = min(arr)

# make an array field sizse
    a = [x for x in range(10)]
    print(a[1])
