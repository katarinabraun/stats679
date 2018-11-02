#!/usr/bin/env python
import math 
import argparse
# use an Argument Parser object to handle script arguments
import doctest

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("--log", action="store_true", help="returns the log of the binomical coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfac(n, k=0): # default value of k = 0 
    """Return the log factorial `log(n!)` for any integer `n>0`.

    Examples: 

    >>> round(logfac(5),2)
    4.79
    >>> round(logfac(0),2)
    0
    >>> round(logfac(5,3),2)
    3.0
    >>> round(logfac(5,5),2)
    0
    >>> round(logfac(6,5),2)
    1.79
    
    Notes: 

    """
    assert type(n)==int, "error message: here n should be an integer"
    assert type(k)==int, "error message: here n should be an integer"
    assert n >= 0, "error message: n must be great than or equal to zero"
    assert k >= 0, "error message: k must be greater than or equal to zero"


    result = 0

    for i in range(k,n):
        result += math.log(i+1) # to start with k (or 1 if k = 0)
    return result

# print(round(logfac(5),2))
# print(round(logfac(0),2))
# print(round(logfac(5,3),2))
# print(round(logfac(5,5),2))
# print(round(logfac(6,5),2))

def choose(n,k,log=False): 
    """Calculate the log of a binomial `log(choose(n,k))` for any integers `n>=0` and `0 <= k <= n`.
    choose(n,k) = n!/(k! (n-k)!) so log(choose(n,k)) = log(n!/k!) - log((n-k)!)

    Examples: 

    >>> round(choose(4,1),2)
    4
    
    >>> round(choose(5,3,True),2)
    2.3

    >>> round(choose(5,3,False),2)
    10

    Notes:
    """
    
    assert type(n)==int, "error message: here n should be an integer"
    assert n >= 0, "error message: n must be great than or equal to zero"
    assert type(k)==int, "error message: here n should be an integer"
    assert (k >= 0) and (k <= n), "error message: k must be greater than or equal to zero and k must be less than or equal to n"
    
    if log: 
        return(logfac(n,k) - logfac(n - k))
    else:
        return(round(math.exp(logfac(n,k) - logfac(n - k))))

def runTests():
    print("testing the module...")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose(args.n, args.k, args.log))