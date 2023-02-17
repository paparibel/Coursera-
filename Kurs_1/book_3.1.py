#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('Enter Hours: '))
rph = float(input('Enter Rate: '))
if hours > 40:
    pay = 40 * rph + ((1.5 * rph)*(hours-40))
    print ('Pay:', pay)
else:
    pay = rph * hours
    print ('Pay:', pay)