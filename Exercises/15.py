#Uppgift: Bygg ett program som frågar efter förnamn, efternamn och land. Funktionen ska rensa mellanslag, kombinera namn, kunna välja lowercase/uppercase och returnera resultatet.
#Challenge: Låt användaren själv välja lower eller upper.
def clean_name(fnamn,enamn,country,case_rule):
    namn=fnamn.strip()+" "+enamn.strip()
    country=country.strip()

    if case_rule == "upper":
        namn=namn.upper()
        country=country.upper()

    elif case_rule == "lower":
        namn=fnamn.lower().capitalize()+ " "+enamn.lower().capitalize()
        country=country.lower().capitalize()

    return namn+" "+country
   

fnamn=input("Ange förnamn: ")
enamn=input("Ange efternamn: ")
country=input("Ange land: ")
case_rule=input("Ange ""lower"" för gemena eller ""upper"" för versaler: ").strip().lower()

print(clean_name(fnamn,enamn,country,case_rule))
