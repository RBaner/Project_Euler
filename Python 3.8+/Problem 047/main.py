#A rotating window that holds the current numbers in view
#avoids recording/recalculating any primefactors as well as 
#the complexity of reorganizing to make it "in order"
from sympy import primefactors
import time

def n_consec_n_distinct_prime_factors(n):
    window = [primefactors(i) for i in range(2,n+2)]
    current = 2
    run = 0
    while True:
        current_factors = primefactors(current)
        window[current%n] = current_factors
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