from math import log2, comb

def S(n):
    total = 0
    for i in range(1,n+1):
        total += ((-2)**i) * comb(2*i,i)
    return(total)

def v2(n): #improve to use bit magic
    n = abs(n)
    r = int(log2(n))
    while r >= 1:
        if n%(2**r) == 0:
            return(r)
        else:
            r -= 1
    raise Exception("Odd number")

def u(n):
    return(v2(3*S(n)+4))

def U(n):
    total = 0
    for i in range(1,n+1):
        if i%100==0:
            print(i)
        total += u(i**3)
    return(total)

def main()->int:
    return(U(10**4))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)