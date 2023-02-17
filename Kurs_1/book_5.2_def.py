#Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.
def fin_min_max():
    najmniejsza = None
    najwieksza = None
    while True:
        num = input('Enter a number: ')
        if num == 'done':
            break
        try:
            num = int(num)
        except:
            print('Invalit input')
            continue
        if najmniejsza is None or num < najmniejsza:
            najmniejsza = num
        if najwieksza is None or num > najwieksza:
            najwieksza = num
    return (najmniejsza, najwieksza)

while True:
    
    min_max = fin_min_max()

    print('Najwieksza to: ', min_max[0])
    print('Najmniejsza to: ', min_max[1])
    
    if min_max[0] == 1 or min_max[1] == 3500:
        break
    
print ('Koniec')
