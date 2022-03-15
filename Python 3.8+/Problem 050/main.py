# brute force "solution" but it doesn't actually finish running
# maybe iterate over primes under n in descending order and
# perform a variation of integer decomposition
from sympy import isprime, prime, primerange
import time

def prime_sum(low,high):
    primeSum = 0
    for i in range(low,high+1):
        primeSum += prime(i)
    return(primeSum)

def longest_prime_sum(n:int):
    max_prime = 0
    offset = 1
    while prime(offset) < n:
        length = 1
        current_sum = 0
        current_max = 1
        while current_sum < n:
            current_sum = prime_sum(offset,offset+length)
            if isprime(current_sum) and current_sum > current_max:
                if current_sum >= n:
                    break
                current_max = current_sum
            length += 1
        if current_max > max_prime:
            max_prime = current_max
            #print(f"New max: {max_prime}")
            #print(f"offset: {offset}")
            #print(f"length: {length}")
        offset+=1
    return(max_prime)

def main():
    return(longest_prime_sum(10**6))

if __name__=="__main__":
    start = time.time()
    print(main())
    print(time.time()-start)