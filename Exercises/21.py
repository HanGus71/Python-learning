#Uppgift:Skapa en dictionary med fem personer och deras ålder. Loopa igenom dictionaryn och skapa en **ny dictionary** som endast innehåller personer som är 50 år eller äldre.
#Challenge: Beräkna medelåldern för personerna i den nya dictionaryn.
#Extra: Låt användaren ange en åldersgräns och använd den för filtreringen.
def sort_over_50(personer):
    personer_age={}
    for name,age in personer.items():
        if age >= age_limit:
            personer_age[name]=age
    return personer_age

def calculate_average_age(personer_age):
    total_age=0
    for name,age in personer_age.items():
        total_age+=age
    return(total_age/len(personer_age))  

personer={"Hans":55,
          "Anna":50,
          "Tommy":45,
          "Annelie":43,
          "Peter":60}

age_limit=int(input("Ange åldersgräns för utsortering: "))
personer_age=sort_over_50(personer)

print(sort_over_50(personer))
print(calculate_average_age(personer_age))
