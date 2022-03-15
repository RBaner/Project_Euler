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

def prime(n):
    prime = 3
    count = 2
    while count < n:
        possible = prime
        while True:
            possible += 1
            if isprime(possible):
                prime = possible
                count+=1
                break
            else:
                continue
    return(prime)
    
if __name__=="__main__":
    start = time.time()
    print(prime(10001))
    print(time.time()-start)