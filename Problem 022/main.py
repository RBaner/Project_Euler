import math
import string

def get_names():
    with open('p022_names.txt','r') as f:
        names = [i for i in f.readline().split(',')]
    names = [i.strip('"') for i in names]
    names.sort()
    return(names)

def score(s):
    total = 0
    for char in s:
        total += string.ascii_uppercase.index(char)+1
    return(total)

def sol():
    names = get_names()
    return(sum([(i+1)*score(names[i]) for i in range(len(names))]))
