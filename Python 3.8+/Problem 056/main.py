def digitSum(n):
    return(sum([int(i) for i in str(n)]))

def maxabDigitSum(n):
    maximum=0
    for a in range(1,n):
        for b in range(1,n):
            summ = digitSum(a**b)
            if summ > maximum:
                maximum = summ
    return(maximum)

def main()->int:
    return(maxabDigitSum(100))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)