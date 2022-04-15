def digitMatchUpTo(n) -> int:
    num = 1
    while True:
        if all([sorted(str(i*num)) == sorted(str(num)) for i in range(1,n+1)]):
            return(num)
        else:
            num+=1

def main()->int:
    return(digitMatchUpTo(6))

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)