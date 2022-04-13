# ith denominator = [i-1] * 2 + [i-2]
# ith numerator = [i-1] * 2 + [i-2]
from math import log10

def p57(n:int) -> int:
    numerators = [3,7]
    denominators = [2,5]
    for i in range(n-2):
        denominators.append(denominators[-1]*2 + denominators[-2])
        numerators.append(numerators[-1]*2 + numerators[-2])
    return(len([i for i in range(len(denominators)) if int(log10(numerators[i])) > int(log10(denominators[i]))]))

def main()->int:
    return(p57(10**3))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)