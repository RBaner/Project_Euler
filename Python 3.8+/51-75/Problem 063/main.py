from math import log10
from itertools import count

def main()->int:
    res = 0
    for power in count(1):
        if int(log10(9**power))+1 == power-1:
            return(res)
        else:
            res += len([int(log10(num**power))+1 for num in range(1,10) if int(log10(num**power))+1 == power])

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)