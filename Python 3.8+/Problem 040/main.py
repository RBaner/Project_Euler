import math

def bruteForceDigitCatch(n):
    if n == 1:
        return(1)
    digit = 0
    digit_count = 0
    while True:
        digit += 1
        digit_count += int(math.log10(digit))+1
        # print(digit)
        # print(digit_count)
        # print("++++++++++++++++++++++++++++++++++")
        if n <= digit_count + int(math.log10(digit+1))+1:
            return(int(str(digit+1)[n-digit_count-1]))

def main():
    catch = [10**i for i in range(7)]
    digits = [bruteForceDigitCatch(i) for i in catch]
    product = 1
    for digit in digits:
        product *= digit
    return(product)

if __name__=='__main__':
    print(main())