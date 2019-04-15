# Implementation of calulation of Reibility of Multicast Under random linear network coding
# Evengy Tsimbalo & Andrea Tassi
# coded by Hosein Kangavar Nazari
import numpy as np
import math


def combination(N, x):
    numerator = math.factorial(N)
    denominator = math.factorial(N-x) * math.factorial(x)
    return numerator/denominator


# q denotes Finite field size , m received packet in decoding matrix, K is number of symbols to decode
def full_rank_probability(q, m, k):
    if m < k:
        return 0
    answer = 1
    for i in range(k-1):
        answer *= 1 - pow(q, i-m)
    return answer

def i_rank_probability


if __name__ == "__main__":
    test = full_rank_probability(2, 15, 10)
    print(test)
