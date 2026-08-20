#Uppgift: Skriv två funktioner som räknar ut summan av två tal: en som bara printar resultatet och en som returnerar resultatet.
#Challenge: Använd den returnerande funktionen i en annan beräkning.
def print_result(tal1,tal2):
    print("Summa från funktion ""print_result"":",tal1+tal2)

    

def return_result(tal1,tal2):
    return tal1+tal2

tal1=int(input ("Ange första talet: "))      
tal2=int(input ("Ange andra talet: "))

print_result(tal1,tal2)

summa=return_result(tal1,tal2)

print("Summa från funktionen ""return_result"": ",summa)
        
tal3=int(input("Ange det tredje talet: "))
summa=summa+int(tal3)
print("Summa från funktionen ""return_result"" och tredje talet: ",summa)