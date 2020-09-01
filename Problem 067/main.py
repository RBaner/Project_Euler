def get_triangle():
    tri = []
    with open('p067_triangle.txt','r') as file:
        for line in file:
            tri.append([int(i) for i in line.split(' ')])
    return(tri)

def sol(mat):
    '''
    This function keeps a tally of the largest total reachable by
    every int at any given level of the triangle. This is a dynamic
    programming solution that solves the problem by solving
    subproblems of smaller traingle sums.
    '''
    totals = [mat[0][0]]
#    print(totals)
    for i in mat[1:]:
        temp = []
        for total in totals:
            temp.append(total)
#        print('****************************')
#        print('i = '+str(i))
        for j in range(len(i)):
#            print('========')
#            print('j = ' + str(j))
            if j == 0:
                temp[0] += i[j]
            elif j != len(i)-1:
                temp[j] = max(i[j]+totals[j],i[j]+totals[j-1])
            else:
                temp.append(i[j]+totals[-1])
#            print(totals)
        totals = temp
    return(max(totals))
