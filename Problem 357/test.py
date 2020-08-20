import sympy

def pgen(n,show=False):
    divisor_list = sympy.divisors(n)
    for i in divisor_list[:int(len(divisor_list)/2)+1]:
            if show:
                print("%d+%d=%d"%(i,int(n/i),i+int(n/i)))
            if not sympy.isprime(i+int(n/i)):
                return(False)
    return(True)


def main(n):
    """Cases below 10 are added manually, after that we first make sure the number
        isn't =4(mod10)(implies a 2^2 in prime factorization)
        or =6(mod10)(implies there exists a d+(n/d) that is divisible
        by 5). Then we screen for numbers for which the mobius function
        returns 1 or -1 so we don't check numbers with non-distinct
        prime factors. Any numbers left are manually checked by pgen(i-1)"""
    output = 1 + 2 + 6
    for i in sympy.primerange(8,n):
        if (i-1)%10 in [2,8,0]:
            if abs(sympy.mobius(i-1)):
                if pgen(i-1):
                    output += (i-1)
    return(output)

def brute_force(n):
    """This function was used for testing purposes and is
        the most naive but surefire way to get the solution sum"""
    output = 0
    for i in range(1,n+1):
        if pgen(i):
            output+=i
    return(output)

def problem():
    """Run this to get the solution sum as well as computation time
        in seconds"""
    start = time.time()
    print(main(100000000))
    end = time.time()
    print(end-start)
