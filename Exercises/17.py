#Uppgift: kapa en funktion `calculate_average(numbers)` som tar emot en lista med tal och returnerar medelvärdet av listan.
#Använd funktionen för att beräkna medelvärdet av `[12, 18, 25, 30, 15]`.
#Challenge: Skapa även en funktion find_max(numbers) som returnerar det största talet utan att använda max().
#Extra: Skapa en funktion count_even(numbers) som räknar hur många jämna tal listan innehåller.
def calculate_average(numbers):
    return(sum(numbers)/len(numbers))

print(calculate_average([12,18,25,30,15]))

def find_max(numbers):
    return sorted(numbers,reverse=True)[0]
  

print(find_max([12,18,25,30,15]))

def count_even(numbers):
    count=0
    for number in numbers:
        if number %2==0:
            count+=1
    return count

print(count_even([12,18,25,30,15]))