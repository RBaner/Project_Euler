#current algorithm: loop all numbers while adding to count of digits
#poptimization: formula to generate nth digit given that we know how many n-digit numbers exists for each n

import math

def main():
    digit_catch = [10**i for i in range(0,7)]
    count = 0
    number = 0
    while True:
        if (count + math.log10(number) in digit_catch):
