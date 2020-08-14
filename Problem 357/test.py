import sympy

def divisors(n):
    if n%2 == 0:
        return([i for i in range(1,n+1) if n%i==0])
    else:
        return([i for i in range(1,n+1,2) if n%i == 0])


def pgen(n,show=False):
    divisor_list = divisors(n)
    for i in divisor_list[:int(len(divisor_list)/2)+1]:
            if show:
                print("%d+%d=%d"%(i,int(n/i),i+int(n/i)))
            if not sympy.isprime(i+int(n/i)):
                return(False)
    return(True)


def main(n):
    output = 1
    for i in range(2,n+1,2):
        if sympy.isprime(i):
            pass
        if pgen(i):
            output+=i
        if i%int(n/10)==0:
            print(i)
    print(output)
