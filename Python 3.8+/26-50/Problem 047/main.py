from sympy import primefactors
import time

def n_consec_n_distinct_prime_factors(n):
    current = 2
    run = 0
    while True:
        current_factors = primefactors(current)
        if len(current_factors) == n:
            run +=1
            if run == n:
                return(current-(n-1))
        else:
            run = 0
        current += 1

def main():
    return(n_consec_n_distinct_prime_factors(4))

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)