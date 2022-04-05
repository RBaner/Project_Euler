# This was partially written by Github copilot
# Having it write functions like isPalindromic and CountLychrelNumbers
# was fun and efficient as they are simply function but when I came to write
# isLychrel it wrote the whole func for me (including the cap of 50 sum attempts)
# which makes me think it pulled it from someone else's answers, not a fan of that.

def isPalindromic(n:int)->bool:
    return(str(n) == str(n)[::-1])

def isLychrel(n:int)->bool:
    for i in range(50):
        n += int(str(n)[::-1])
        if isPalindromic(n):
            return(False)
    return(True)

def CountLychrelNumbers(n:int)->int:
    count = 0
    for i in range(1,n+1):
        if isLychrel(i):
            count += 1
    return(count)

def main()->int:
    return(CountLychrelNumbers(10**4))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)