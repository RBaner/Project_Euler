#not working

from itertools import combinations
from math import log10
from sympy import isprime

def findPrimeFamilySeed(n)->int:
    found = False
    current_num = 1
    maximum = 0
    while not found:
        for r in range(1,int(log10(current_num))+1):
            for indicies in combinations([i for i in range(int(log10(current_num))+1)],r):
                current_num_string = str(current_num)
                #calculate family size by taking length of list comprehension, allow elements to pass into list by 
                #boolean isprime
                current_maximum = len([])


        current_num += 1


def main()->int:
    return(findPrimeFamilySeed(8))

    

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)