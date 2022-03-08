#SLOW
#There has to be a mathematical way to speed things up/constrict the possibilities
#perhaps not worth it to store pent numbers and instead generate them as needed
import time
from math import sqrt

def increase_pentagonal_numbers(current_state: list,upper_bound: int) -> list:
    while max(current_state) < upper_bound:
        nextNumber = int(0.5 * (len(current_state)+1) * (3*(len(current_state)+1)-1))
        current_state.append(nextNumber)
    return(current_state)

def is_pent(x):
	f = (.5 + sqrt(.25+6*x))/3
	if f - int(f) == 0:
		return True
	else:
		return False

def main() -> int:
    pentagonalNumbers = [1,5]
    pentagonalNumbers = increase_pentagonal_numbers(pentagonalNumbers,150)
    for i in pentagonalNumbers:
        #print(i)
        if i == max(pentagonalNumbers):
            pentagonalNumbers = increase_pentagonal_numbers(pentagonalNumbers,max(pentagonalNumbers)*2)
            print(len(pentagonalNumbers))
        for j in pentagonalNumbers[:pentagonalNumbers.index(i)]:
            summ = i + j
            diff = i - j
            if summ >= max(pentagonalNumbers) or diff >= max(pentagonalNumbers):
                pentagonalNumbers = increase_pentagonal_numbers(pentagonalNumbers,max(summ,diff) + 1)
            if summ in pentagonalNumbers and diff in pentagonalNumbers:
                return(abs(i-j))

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)