from math import sqrt

def is_tri(x:int)-> bool:
    return(((sqrt(8*x+1)-1)/2)%1==0)

def is_square(x:int)-> bool:
    return((sqrt(x))%1==0)

def is_pent(x:int)-> bool:
    return(((sqrt(24*x+1)+1)/6)%1==0)
	    
def is_hex(x: int) -> bool:
	return(((sqrt(8*x + 1)+1)/4)%1==0)

def is_hept(x: int) -> bool:
	return(((sqrt(40*x+9)+3)/10)%1==0)

def is_oct(x: int) -> bool:
	return(((sqrt(3*x+1)+1)/3)%1==0)

def cyclic_set(n:int,debug:bool) -> int:
    funcs = [is_tri,is_square,is_pent,is_hex,is_hept,is_oct]
    values = []
    for func in funcs[:n]:
        values.append([i for i in range(1000,10000) if func(i)])
    res = 0
    def recur_search(visited_cats: list, current: list,debug:bool):
        if len(current) == len(values)-1 and debug:
            print(current)
            print(visited_cats)
        if len(current) == len(values):
            if debug:
                print(current)
            yield(sum(current))
        for i,cat in enumerate(values):
            if i in visited_cats:
                continue
            for num in cat:
                if num in current:
                    continue
                if len(current) != len(values)-1: 
                    if num%100 == current[0]//100:
                        yield(max(recur_search(visited_cats + [i],[num]+current,debug)))
                    if current[-1]%100 == num//100:
                        yield(max(recur_search(visited_cats + [i],current+[num],debug)))
                elif current[-1]%100 == num//100 and num%100 == current[0]//100:
                        yield(max(recur_search(visited_cats + [i],current+[num],debug)))
        yield(0)
    for i,cat in enumerate(values):
        for num in cat:
            res = max(*[i for i in recur_search([i],[num],debug)],res)
    return(res)

def main()->int:
    return(cyclic_set(6,0))

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)
