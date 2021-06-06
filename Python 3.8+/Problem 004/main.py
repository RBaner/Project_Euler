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
    current = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(i*j) and (i*j)>=current:
                current = i*j
    return(current)
