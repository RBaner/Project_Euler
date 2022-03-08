from sympy import isprime
from math import sqrt
import time

def main():
    num = 3
    while True:
        if num%2 == 0:
            num += 1
            continue
        elif isprime(num):
            num += 1
            continue
        else:
            passed = False
            for i in range(1,int(sqrt((num-3)/2))+1):
                if isprime(num-2*(i**2)):
                    passed = True
                    break
            if passed== False:
                return(num)
            num+=1

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)