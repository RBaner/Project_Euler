def main(n):
    checked = []
    for i in range(2,n+1):
        if sum([int(j)**5 for j in str(i)]) == i:
            checked.append(i)
    return(checked)
