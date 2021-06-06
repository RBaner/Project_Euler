def fib(n):
    if n in [1,2]:
        return(1)
    else:
        record = [1,1]
        for i in range(n-2):
            record.append(record[-1]+record[-2])
        return(record[-1])

def sol():
    index = 1
    while True:
        if len(str(fib(index))) >= 1000:
            return(index)
            break
        index += 1
