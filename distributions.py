#import math
import random
import scipy.special as ss

def U () :
    u = random.random()
    return u
def MyBernoulli (p) :
    u = U()
    if (u < p) :
        x = 1
    else :
        x = 0
    return x

def MyBinomial (n, p) :
    trials = [MyBernoulli(p) for i in range(n)]
    return sum(trials)

def MyGeometric (p) :
    x = 1
    while (MyBernoulli(p) == 0) :
        x += 1
    return x

def MyNegativeBinomial (k, p) :
    geomlist = [MyGeometric(p) for i in range(k)]
    return sum(geomlist)

def MyPoisson (l) :
    u = U()
    i = 0
    s = exp(-l)
    while (u >= s) :
        i += 1
        s += exp(-l)*(l**i)/factorial(i)
    return i

def MyExponential (l) :
    u = U()
    return (-log(u))/l

def MySampleBeta () :
    alpha = 5.5
    beta = 3.1
    c = 2.5
    X = U()
    Y = c * U()
    while (Y > X^(alpha-1) * (1-X)^(beta-1) / ss.beta(alpha,beta)) :
        X = U()
        Y = c * U()
    return X

def MySampleStandardNormal () :
    a = -3
    b = 3
    X = -3+6*U()
    Y = U()
    while (Y > exp(-(X**2)/2)) :
        X = -3+6*U()
        Y = U()
    return X