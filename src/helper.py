# -*- coding: UTF-8 -*-

def binomial_coefficient(n, k):
    if k<0 or k>n:
        return 0
    if k==0 or k==n:
        return 1
    k = min(k, n-k)
    c = 1
    for i in range(k):
        c = c*(n-i)/(i+1)
    return c
