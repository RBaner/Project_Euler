def digitSum(n):
    return(sum([int(i) for i in str(n)]))

maximum=0
for a in range(1,100):
    for b in range(1,100):
        summ = digitSum(a**b)
        if summ > maximum:
            maximum = summ

print(maximum)
