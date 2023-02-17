#Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.
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
        
print('Najwieksza to: ', najwieksza)
print('Najmniejsza to: ', najmniejsza)