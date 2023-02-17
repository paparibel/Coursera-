#Exercise 6: Rewrite your pay computation with time-and-a-half for over-
#time and create a function called computepay which takes two parameters
#(hours and rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
def computepay(hours, rph): 
    if hours > 40:
        pay = 40 * rph + ((1.5 * rph)*(hours-40))
    else:
        pay = rph * hours
    return pay

while True:
    try:
        hours = float(input('Enter Hours: '))
        rph = float(input('Enter Rate: '))
        break
    except ValueError: #ValueError jest rodzajem wyjątku w języku Python, który jest zgłaszany, gdy funkcja próbuje przetworzyć argument, który ma poprawny typ, ale nieprawidłową wartość. Wyjątek ten jest często używany w sytuacjach, gdy program musi przetworzyć dane wejściowe, ale dane te nie są zgodne z oczekiwaniami.
        print ('Enter numeric input')
            
totalpay =computepay(hours, rph)
print ('Pay:', totalpay)
    