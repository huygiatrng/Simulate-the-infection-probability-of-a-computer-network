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
