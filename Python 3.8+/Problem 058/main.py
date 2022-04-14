from sympy import isprime

def spiral_sum(threshold: float, debug = False) -> int:
    prime_counter = 0
    counter = start = 1
    diff = 2
    while True:
        for i in range(1,5):
            current_number = start+diff*i
            counter += 1
            if isprime(current_number):
                prime_counter += 1
            if i==4:
                start = current_number
            if debug:
                print(f"Current number: {current_number}")
                print(f"Current ratio: {prime_counter/counter}")
                print(f"Current diff: {diff}")
            if (prime_counter/counter) < threshold:
                return(diff+1)
        diff += 2

if __name__=="__main__":
    from time import time
    start = time()
    print(spiral_sum(0.1))
    end = time()
    print(end-start)