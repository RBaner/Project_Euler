from sympy import isprime
from itertools import permutations
import time

digits = [int(i) for i in "123456789"]

def numFromList(listOfDigits: list) -> int:
    output = 0
    power = len(listOfDigits)-1
    for digit in listOfDigits:
        output += digit * (10**power)
        power -= 1
    return(output)

def main() -> int:
    maximum = []
    for n in range(len(digits)):
        if n not in [4,7]:  #all other lengths of pandigitals fall vitcim to 3-divisibility (barring length 1)
            continue
        possible = [numFromList(permutation) for permutation in permutations(digits[:n])]
        possible = [number for number in possible if isprime(number)]
        try: 
            maximum.append(max(possible))
        except Exception as e:
            continue
    return(max(maximum))

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)