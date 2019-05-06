# Implementation of calulation of Reibility of Multicast Under random linear network coding
# wroted by Evengy Tsimbalo & Andrea Tassi
# Coded by Hosein Kangavar Nazari (IASBS university)

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


def thildaProbability(m, mu, q, k):
    answer = 0
    for i in range(0, min(m)+1):
        iTemp = i_rank_probability(q, mu, k, i)
        seperateRankTemp = 1
        for j in range(0, len(m)):
            seperateRankTemp *= full_rank_probability(q, m[j]-mu, k - i)
        answer += iTemp * seperateRankTemp
    return answer
    


# m  an array of pocket received by each receiver, N total packet sent, e an array of error between each link


def phi(m, N, e):
    answer = 1
    for i in range(0, len(m)):
        answer *= pow((1 - e[i]), m[i]) * pow(e[i], N-m[i])
    return answer


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


def finialPossibleSet(tempSet, N):
    for i in range(len(tempSet)):
        if tempSet[i] != N:
            return False
    return True


def everyPossibleSet(N, L):
    result = []
    buckets = [0] * L
    temp = buckets[:]
    result.append(temp)
    while True:
        i = 0
        for j in range(0, N):
            buckets[i] += 1
            temp = buckets[:]
            result.append(temp)
            # is it finished
            flag = finialPossibleSet(temp, N)
            if flag:
                return result
        # search for another element which is not N
        for k in range(0, L):
            if(buckets[k] < N):
                buckets[k] += 1
                for ii in range(0, k):
                    buckets[ii] = 0
                temp = buckets[:]
                result.append(temp)
                break

    return result


if __name__ == "__main__":
    # ***********************************************************************************************
    # FIELD_SIZE = 2
    # NUMBER_OF_TOTAL_TRANSMISSION = 20
    # NUMBER_OF_RECEIVERS = 3
    # # in order to decode we have to at least send number of symbols
    # NUMBER_OF_SYMBOLS = 5

    # # we consider every link has a same amount of error rate
    # ERROR_RATE = 0. 10
    # errorSet = [ERROR_RATE for i in range(0, NUMBER_OF_RECEIVERS)]

    # FINAL_ANSWER = 0

    # # every possible set of number of received codes by nodes
    # # first parameter: Number of total transmission
    # # Second parameter: Number of receiver nodes
    # M = everyPossibleSet(NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS)
    

    # for m_i in M:
    #     tempPhi = phi(m_i, NUMBER_OF_TOTAL_TRANSMISSION, errorSet)
    #     tempBeta = None
    #     tempPThilda = None
    #     innerAnswer = 0 
    #     for mu in range(0, min(m_i)):
    #         tempPThilda = thildaProbability(m_i,mu,FIELD_SIZE,NUMBER_OF_SYMBOLS)
    #         tempBeta = ncr(NUMBER_OF_TOTAL_TRANSMISSION, mu) * beta(m_i,
    #                                                                 mu, NUMBER_OF_TOTAL_TRANSMISSION, NUMBER_OF_RECEIVERS)
    #         innerAnswer += tempPThilda * tempBeta
        
    #     FINAL_ANSWER += innerAnswer * tempPhi 

    #         # FINAL_ANSWER +=

    #         # make an array field sizse
    # # a = [x for x in range(10)]
    # # print(a[1])
    # print (FINAL_ANSWER)
    # ***********************************************************************************************
    print(phi([3,4,6],10,[0.3 for i in range(3)]));
    # print(ncr(10,1))