import time
from itertools import permutations
from sympy import isprime, primerange

def num_to_list(n:int) -> list:
    return([int(i) for i in str(n)])

def list_to_num(l:list) -> int:
    output = 0
    for i in range(len(l)):
        output += l[-(i+1)] * (10**(i))
    return(output)

def has_arithmetic_seq(l: list) -> list:
    pairs = [[l[i],l[j]] for i in range(len(l)) for j in range(i,len(l))]
    seen = []
    for pair in pairs:
        difference = abs(pair[0]-pair[1])
        low_pair = [min(pair) - difference] + pair
        hi_pair = pair + [max(pair) + difference]
        if (difference == 0) or (hi_pair in seen) or (low_pair in seen):
            continue
        elif (min(pair) - difference in l):
            seen.append(low_pair)
            yield(low_pair)
        elif (max(pair) + difference in l):
            seen.append(hi_pair)
            yield(hi_pair)

def main() -> int:
    seen = []
    perm_classes = []
    for prime in primerange(1000,10000):
        prime_perm_list = [list_to_num(i) for i in permutations(num_to_list(prime)) if isprime(list_to_num(i)) and list_to_num(i) > 1000]
        if min(prime_perm_list) in seen:
            continue
        else:
            seen.append(min(prime_perm_list))
        perm_classes.append(sorted(list(set(prime_perm_list))))
    for perm_class in perm_classes:
        for arithmetic_seq in has_arithmetic_seq(perm_class):
            if 1487 in arithmetic_seq:
                continue
            else:
                return(''.join(str(num) for num in arithmetic_seq))

if __name__=="__main__":
    start = time.time()
    print(main())
    print(time.time()-start)