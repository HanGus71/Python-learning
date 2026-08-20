#Uppgift: Skapa clean_person(first_name, last_name, country) som rensar namn med strip(), gör namnet lowercase och returnerar en dictionary med name och country.
#Challenge: Lägg till parametern case_rule med standardvärdet "lower".
def pers_info(first_name,last_name,country,case_rule):
        first_name=first_name.strip()
        last_name=last_name.strip()

        if case_rule == "upper":
            first_name=first_name.upper()
            last_name=last_name.upper()

        elif case_rule == "lower":
            first_name=first_name.lower().capitalize()
            last_name=last_name.lower().capitalize()

        elif case_rule == "":
            first_name=first_name.lower().capitalize()
            last_name=last_name.lower().capitalize()

        name_country={"name":first_name + " "+ last_name,
                      "country":country}
        return name_country

name_country=pers_info(
        input("Ange förnamn: "),
        input("Ange efternamn: "),
        input("Ange land: "),
        input("Ange upper för stora och lower för små: ")
)
print(name_country)