from math import sqrt

def sqrt_seq_period(n:int) -> int:
    seq = []
    seq.append(sqrt(n))
    cycle_detect = []
    while True:
        a = 1/(seq[-1] - int(seq[-1]))
        if a//0.001 in cycle_detect:
            seq[-1] = int(seq[-1]) 
            return(len(seq[cycle_detect.index(a//0.001)+1:]))
        cycle_detect.append(a//0.001)   
        seq.append(a)
        seq[-2] = int(seq[-2])

def odd_sqrt_period_count_under(limit:int) -> int:
    res = 0
    for i in range(2,limit+1):
        if sqrt(i)%1==0:
            continue
        if sqrt_seq_period(i)%2!=0:
            res += 1
    return(res)


def main()-> int:
    return(odd_sqrt_period_count_under(10000))

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)