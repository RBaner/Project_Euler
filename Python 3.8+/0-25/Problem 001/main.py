
def multiple_sum(multiples:list,limit:int) -> int:
    res = 0
    for i in range(1,limit):
        if any([i%multiple==0 for multiple in multiples]):
            res += i
    return(res)

def main() -> int:
    return(multiple_sum([3,5],1000))

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)