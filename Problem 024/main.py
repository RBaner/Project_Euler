import math

def lex(n,num):
    """
    This is a recursive algorithm to determine the lexicographic
    arrangement based on a starting set and a lexicographic position.
    The main idea is to determine the leading digit by dividing by
    the factorial of the size of the set-1
    e.g. for [0,1,2] we have the following arrangements
    012 021 102 120 201 210
    for which we can see thet are divided into pairs based on leading digit.
    They are in pairs because 2! = 2
    """
    #n is the lexicographic position
    #num is the numbers being arranged
    if len(num) == 1:
        return(num)
    else:
        factorial = math.factorial(len(num)-1)
        pos = n//factorial
        #this little weird assignment mess is because
        #of python's weird way of assigning variables
        #if i assigned variable digit and then removed it
        #from the list num, digit would retroactivley change
        #e.g. try this
        #test = [1,2,3]
        #temp = test[1]
        #print(temp)
        #test.remove(2)
        #print(temp)
        digit = num[pos]
        new_num = num
        new_num.remove(num[pos])
        #
        return([digit] + lex(n%factorial,new_num))
