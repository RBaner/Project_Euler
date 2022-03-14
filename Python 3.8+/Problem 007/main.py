import time
from math import sqrt

def isprime(n):
    if n%2 == 0:
        if n == 2:
            return(True)
        else:
            return(False)
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0:
                return(False)
        return(True)

def main():
    primes = [2,3,5]
    while len(primes) <= 10001:
        possible = primes[-1]
        while True:
            possible += 1
            if isprime(possible):
                primes.append(possible)
                break
            else:
                continue
    return(primes[10000])
    
if __name__=="__main__":
    start = time.time()
    print(main())
    print(time.time()-start)