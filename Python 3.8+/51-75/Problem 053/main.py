# potential optimization in recognizing the fact that if an element is >10**6 all future elements that are affected by it are also >10**6
# creating a waterfall like effect of elements that need not be computed

def PascalsTriangle(n): #dynamic generation of pascals triangle
    triangle = [[1]]
    for line in triangle:
        newLine = [1]*(len(line)+1)
        for element in range(1,len(line)):
            newLine[element] = line[element-1] + line[element]
        triangle.append(newLine)
        if len(triangle) >= n:
            return(triangle)

def p53() -> int: #nCr is the r-th item of the n-th row in pascals triangle (counting starting from 0 which is why we generate 101 rows of pascals triangle)
    triangle = PascalsTriangle(101) 
    counter = 0
    for line in triangle:
        for element in line:
            if element > 10**6:
                counter +=1
    return(counter)

def main()->int:
    return(p53())

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)