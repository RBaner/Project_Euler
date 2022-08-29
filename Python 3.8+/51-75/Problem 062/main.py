# Lesson: Avoid making ALL permutatiobs whenever possible
# Potential improvement: rework to avoid all the string<->int conversions

from itertools import permutations
from math import log10

def list_to_int(l:list) -> int:
    res = 0
    place = 0
    for i in l[::-1]:
        res+= i*(10**place)
        place += 1
    return(res)

def power_permutations(power: int,num_of_permutations: int) -> int:
    current_powers = []
    num = 1
    while True:
        while int(log10(num**power)) == int(log10((num+1)**power)):
            current_powers.append(num**power)
            num += 1
        current_powers.append(num**power)
        while current_powers:
            perms = [i for i in current_powers if sorted(list(str(i))) == sorted(list(str(current_powers[0])))]
            if not perms:
                current_powers.remove(current_powers[0])
            if len(perms) == num_of_permutations:
                return(min(perms))
            else:
                for perm in perms:
                    current_powers.remove(perm)
        current_powers.clear()
        perms.clear()
        num+=1 

def main() -> int: 
    return(power_permutations(3,5))

if __name__=="__main__":
    from time import perf_counter
    start = perf_counter()
    print(main())
    print(perf_counter()-start)
