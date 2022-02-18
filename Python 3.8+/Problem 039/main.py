import math

def main(maximum):
    #define all squares < max
    #1.75 was just arbitrary to keep the sums just above 1000 and fast
    squares = [i for i in range(2,int(maximum**1.75)) if math.sqrt(i)%1 == 0]
    count = {}
    for i in range(len(squares)-2):
        for j in range(i+1,len(squares)-1):
            for k in range(j+1,len(squares)):
                #check if pythagorean triple
                if (squares[i] == squares[j] + squares[k]) or (squares[i] + squares[j] == squares[k]) or (squares[j]==squares[i] + squares[k]):
                    a = int(math.sqrt(squares[i]))
                    b = int(math.sqrt(squares[j]))
                    c = int(math.sqrt(squares[k]))
                    total = a+b+c
                    #add to dict, count{sum: [amount of triples that sum to it, [list of triples as tuples]]}
                    if total in count:
                        count[total][0] += 1
                        count[total][1].append((a,b,c))
                    else:
                        count[total] = [1,[(a,b,c)]]
    #find sum with max number of corresponding triples
    max_ = 0
    max_sum = 0
    for i in count:
        if count[i][0] > max_ and i <= maximum:
            max_ = count[i][0]
            max_sum = i
    return(f'{max_sum} with {max_} and {count[max_sum][1]}')
    #return(count)

if __name__=='__main__':
    print(main(int(input("Sum maximuim: "))))