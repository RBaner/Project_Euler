from math import log10

def main()->int:
    num = 1
    power = 1
    match = set()
    while True:
        while int(log10((num+1)**power))+1 <= power:
            if int(log10(num**power))+1 == power:
                match.add(num)
            if int(log10(2**power))+1 > power:
                return(len(match))
            num+=1
        power+=1

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)