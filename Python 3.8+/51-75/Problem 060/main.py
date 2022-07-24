# Proposed improved solution:
# create hashmap from primes to a list of other primes they can succesfully concat with
# then go with the original 5 deep nested loop using the hashmap to speed up the process
from sympy import primerange, isprime
from itertools import combinations
primes = [i for i in primerange(10000)]

def is_prime_group(prime_list: list) -> bool:
    for comb in combinations(prime_list,2):
        if any([not isprime(int(str(comb[0])+str(comb[1]))), not isprime(int(str(comb[1])+str(comb[0])))]):
            return(False)
    return(True)

def main(n:int) -> int:
    res = primes[-1]*5
    for comb in combinations(primes,5):
        if is_prime_group(comb):
            res = min(res,sum(comb))
    print(res)
    

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main(5))
    print(perf_counter()-start)
