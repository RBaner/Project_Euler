# A much prettier and faster solution but not fast by any means.
# Potential optimizations: improve space complexity by working around storing primes up to n
#                          improve time complexity by modulating offset and length intelligently to get the desired sum/determine sum not possible
from sympy import isprime, prime, primerange
import time

def longest_prime_sum(n:int):
    max_count = 0
    max_prime = 0
    offset = 0
    primes = [i for i in primerange(n)]
    while True:
        for length in range(max_count,len(primes[offset:])):
            current_count = length-offset
            current_sum = sum(primes[offset:length])
            if current_sum > n:
                if current_count < max_count:
                    return(max_prime)
                else: continue
            elif isprime(current_sum):
                if max_count < current_count:
                    max_count = current_count
                    max_prime = current_sum
        offset+=1

def main():
    return(longest_prime_sum(10**6))

if __name__=="__main__":
    start = time.time()
    print(main())
    print(time.time()-start)