#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
suma = 0
ilosc_petli = 0
while True:
    num = input('Podaj wartość, lub wpisz one')
    if num == 'Done':
        break
    try:
        num = int(num)
    except:
        print('Invalid Input')
        continue
    ilosc_petli = ilosc_petli + 1
    suma = suma + num
print('Suma:', suma, '', 'Ilość pentli:', ilosc_petli, '', 'Srednia:', (suma / ilosc_petli))