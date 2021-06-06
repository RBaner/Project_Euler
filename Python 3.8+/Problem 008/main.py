def main(number):
    maximum = 0
    current = ''
    for i in range(len(num)-12):
        if product(number[i:i+13]) >= maximum:
            maximum = product(number[i:i+13])
            current = number[i:i+13]
    return(current + " = " + str(maximum))
