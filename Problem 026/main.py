def f(n,d):
    """
    Takes n/d as fractional input, returns [remainder,digits in sol]
    """
    if d==n:
        return([0,1])
    elif n<d:
        digits = 0
        while n<d:
            n *= 10
            digits += 1
        return([n%d,"0"*(digits-len(str(n//d)))+str(n//d)])
    elif n>d:
        return([n%d,"0"*(digits-len(str(n//d)))+str(n//d)])

def recurrCycleLength(d):
    """
    naive cycle detection using a counting array
    """
    previous = [1]
    reptend = []
    for i in previous:
        new = f(i,d)
        if new[0] == 0:
            return(0)
        if new[0] in previous:
            previous.append(new[0])
            reptend.append(new[1])
            #print(reptend)
            return(len("".join(reptend[previous.index(new[0]):])))
        else:
            previous.append(new[0])
            reptend.append(new[1])
