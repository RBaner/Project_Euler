#! python
import math
98765

# print(sum_1_to_n(1))
# print(sum_1_to_n(2))
# print(sum_1_to_n(3))
# print(sum_1_to_n(4))

def construct_pandigital(num, n):
    return int("".join([str(num * i) for i in range(1,n+1)]))
    
def is_pandigital(num):
    return len(str(num)) == 9 and all([(i in str(num)) for i in "987654321"])

def get_max_n(num):
    return int(math.ceil(9 / len(str(num))))

print(construct_pandigital(192, 3))
print(construct_pandigital(9, 5))

print(get_max_n(192))
print(get_max_n(9))

max = 0
for i in range(1, 9876):
    for max_n in range(1, get_max_n(i)+1):
        pandigital = construct_pandigital(i, max_n)
        if is_pandigital(pandigital):
            print(i, pandigital)
            if pandigital > max:
                max = pandigital
print('\n', max)
