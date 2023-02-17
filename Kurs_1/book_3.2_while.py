#book 3.2.py troche zmodyfikowany, Aby zoptymalizować ten kod, można go nieznacznie zmodyfikować. Zamiast wywoływać funkcję quit(), która natychmiast kończy program, można wprowadzić pętlę while, która umożliwi użytkownikowi ponowne wprowadzenie poprawnych wartości. Na przykład:
while True:
    try:
        hours = float(input('Enter Hours: '))
        rph = float(input('Enter Rate: '))
        break
    except ValueError: #ValueError jest rodzajem wyjątku w języku Python, który jest zgłaszany, gdy funkcja próbuje przetworzyć argument, który ma poprawny typ, ale nieprawidłową wartość. Wyjątek ten jest często używany w sytuacjach, gdy program musi przetworzyć dane wejściowe, ale dane te nie są zgodne z oczekiwaniami.
        print ('Enter numeric input')
        
if hours > 40:
        pay = 40 * rph + ((1.5 * rph)*(hours-40))
        print ('Pay:', pay)
else:
        pay = rph * hours
        print ('Pay:', pay)