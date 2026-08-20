#ppgift: Skapa en dictionary för en person med name, age, country och city. Skriv ut varje värde via dess key.
#Challenge: Låt användaren ändra stad och lägga till language.
person={"name":"Hans","age":55,"country":"Sweden","city":"Kode"}
print(person)
print(person["name"])
print(person["age"])
print(person["country"])
print(person["city"])
person["city"]=input("Ändra stad: ")
person["language"]=input("Lägg till språk: ")
print(person)