#Lesson learned: Never memoize what can be generated quickly
import time
from math import sqrt

pent = lambda x: int(x * (3*x - 1)/2)

def is_pent(x):
	f = (.5 + sqrt(.25+6*x))/3
	if f - int(f) == 0:
		return True
	else:
		return False

def main() -> int:
    current = 2
    while True:
        currentPent = pent(current)
        for i in range(1,current):
            if is_pent(currentPent - pent(i))  and is_pent(currentPent + pent(i)):
                return(abs(currentPent - pent(i)))
        current += 1

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)