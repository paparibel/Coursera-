#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
def computergrade(score):
    if score <0.0 or score > 1.0:
        return 'Error: Score is out of range'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'
while True:
    x = input('Podaj wartość między 0.0, a 1.0')
    try:
        x = float(x)
        break
    except ValueError: 
        print('Liczba ma być dziesiętna')
grade = computergrade(x)
print ('Grade:', grade)
        
    