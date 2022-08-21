from math import sqrt

def isprime(n):
    if n%2 == 0:
        if n == 2:
            return(True)
        else:
            return(False)
    else:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0:
                return(False)
        return(True)

def main():
    sum = 2
    for i in range(3,2*(10**6)+1,2):
        if isprime(i):
            sum+=i
    return(sum)

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)