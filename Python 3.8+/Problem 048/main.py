import time

def last_ten_digits(n:int) -> int:
    output = 0
    for i in range(1,n+1):
        output = (output + (i**i))%(10**10)
    return(output)

def main()->int:
    return(last_ten_digits(1000))

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)