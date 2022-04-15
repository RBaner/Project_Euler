# I hate digit replacement and will never touch this code again in my life unless under duress

from itertools import combinations
from math import log10
from sympy import isprime,prime

def findPrimeFamilySeed(n)->int:
    current_prime_counter = 1
    while True:
        current_num = prime(current_prime_counter)
        for r in range(1,int(log10(current_num))+1):
            for indicies in combinations([i for i in range(int(log10(current_num)))],r):
                family = [1]*10
                if int(log10(current_num)) in indicies:
                    break
                run = 0
                for digit in range((1 if 0 in indicies else 0),10):
                    current_num_string = str(current_num)
                    for i in indicies:
                        current_num_string = current_num_string[:i] + str(digit) + current_num_string[i+1:]
                    if isprime(int(current_num_string)):
                        family[digit] = int(current_num_string)
                        run += 1
                if run == n:
                    return(min([i for i in family if i!=1]))
        current_prime_counter += 1

def main()->int:
    return(findPrimeFamilySeed(8))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)