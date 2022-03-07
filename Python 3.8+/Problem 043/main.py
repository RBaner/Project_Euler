#I think a recursive tree generation might be useful here in that we can find all d1d2d3 numbers that
#satisfy the requirement and create sub trees from each of those only using availble digits
from itertools import permutations
import sympy
import time

def number_is_validated(n: int, tests: dict) -> bool:
    for i in range(9,2,-1):
        if (n%10**i)//10**(i-3)%tests[i] != 0:
            return(False)
    return(True)

def num_from_list(listOfDigits: list) -> int:
    output = 0
    power = len(listOfDigits)-1
    for digit in listOfDigits:
        output += digit * (10**power)
        power -= 1
    return(output)

def main() -> int:
    digits = [i for i in range(0,10)]
    tests = {i:sympy.prime(10-i) for i in range(9,2,-1)}
    possible = [num_from_list(permutation) for permutation in permutations(digits)]
    possible = [i for i in possible if number_is_validated(i,tests)]
    return(sum(possible))

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)