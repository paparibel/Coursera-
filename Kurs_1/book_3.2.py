#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:
try:
    hours = float(input('Enter Hours: '))
    rph = float(input('Enter Rate: '))
except:
    print ('Enter numeric input')
    quit()
if hours > 40:
    pay = 40 * rph + ((1.5 * rph)*(hours-40))
    print ('Pay:', pay)
else:
    pay = rph * hours
    print ('Pay:', pay)