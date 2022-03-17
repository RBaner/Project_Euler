#runtime 0.3 -> 0.000998
from time import time

def isPalindrome(n):
    nstring = str(n)
    if len(nstring)%2==0:
        for i in range(int(len(nstring)/2)):
            if nstring[i] != nstring[-(i+1)]:
                return(False)
    else:
        for i in range(int(len(nstring)/2)+1):
            if nstring[i] != nstring[-(i+1)]:
                return(False)
    return(True)

def main():
    current_max = 0
    for i in range(1000,100,-1):
        if i*1000 < current_max:
            return(current_max)
        for j in range(1000,i,-1):
            current = i*j
            if (current)>=current_max:
                if isPalindrome(current):
                    current_max = current
            else:
                break
    return(current_max)

if __name__=='__main__':
    start = time()
    print(main())
    print(time()-start)
