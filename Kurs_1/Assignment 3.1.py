#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
hrs = input('Podaj liczbę godzine:')
hrs = float(hrs)
payh = input('Podaj stawkę za godzine')
payh = float(payh)

if hrs <= 40:
    a = hrs * payh
    print('Wynagrodzenie wynosi: ', a)
elif hrs > 40:
    a = 40 * payh ##Tutaj robie multi razy te hrs powyzej 40h... trzeba dojsc do tego, ale to juz jutro. 
    b = hrs - 40.0 
    c = a + (b * 1.5 * payh)
    print(c)   