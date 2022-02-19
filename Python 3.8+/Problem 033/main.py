#iteration 1 uses strings to make digit replacement easier
#improvements could easily make this a simple double for loop with no function calls and modular arithmetic to replace string manipulation 
#Additionally the double for loop currently includes fractions >1 so limiting the second loop could speed things up
import math
from fractions import Fraction

def common_digit(a,b):
    for i in a:
        for j in b:
            if i==j:
                return(True)
    return(False)

def remove_common_digit(num,denom):
    for digit in num:
        for digit_ in denom:
            if digit == digit_:
                return([num.replace(digit,"",1),denom.replace(digit,"",1)])

def main():
    digits = "0123456789"
    numbers = [('' if i == '0' else i)+j for i in digits for j in digits]
    fractions = [[i,j] for i in numbers for j in numbers if (i!=j and common_digit(i,j) and len(i) == 2 and len(j) ==2)]
    product = 1
    for num in fractions:
        try:
            reduced_num = remove_common_digit(num[0],num[1])
            if Fraction(int(num[0]),int(num[1])) == Fraction(int(reduced_num[0]),int(reduced_num[1])):
                if int(num[0])%10 != 0 and int(num[0]) < int(num[1]):
                    product *= Fraction(int(num[0]),int(num[1]))
        except Exception as e:
            continue
    return(product)

if __name__=='__main__':
    print(main())