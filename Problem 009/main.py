for m in range(500):
    for n in range(m+1):
        if (m**2-n**2)+(2*m*n)+(n**2+m**2) == 1000:
            print("%d,%d"%(m,n))
