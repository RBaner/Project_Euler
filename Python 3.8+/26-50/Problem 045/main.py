from math import sqrt
import time

tri = lambda x : int(x*(x+1)/2)

def is_pent(x) -> bool:
	f = (.5 + sqrt(.25+6*x))/3
	if f - int(f) == 0:
		return True
	else:
		return False
	    
def is_hex(x: int) -> bool:
	f = (sqrt(8*x + 1)+1)/4
	if f - int(f) == 0:
		return True
	else:
		return False

def main() -> int:
    iter = 286
    while True:
        triangle_number = tri(iter)
        if is_hex(triangle_number) and is_pent(triangle_number):
            return(triangle_number)
        iter += 1

if __name__=="__main__":
    start = time.time()
    print(main())
    end = time.time()
    print(end-start)