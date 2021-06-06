#p27

from sympy import isprime
from numba import jit
import time

@jit(nopython=True)
def f(n,a,b):
	return(n**2+a*n+b)

def test(a,b):
	n = 0
	count = 0
	while isprime(f(n,a,b)):
		count+=1
		n+=1
	return(count)

def main():
    maximum = [0,[None,None]]
    for i in range(-999,1000):
            for j in range(-1000,1001):
                    if test(i,j) > maximum[0]:
                            maximum[0] = test(i,j)
                            maximum[1] = [i,j]
    return(maximum[1][0]*maximum[1][1])

def timer():
    start = time.time()
    main()
    end = time.time()
    return(end-start)
