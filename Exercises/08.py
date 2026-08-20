#Uppgift: Skapa en lista med fem städer. Lägg till en sjätte stad, ta bort en stad och skriv därefter ut antal städer samt första och sista staden.
#Challenge: Låt användaren lägga till tre städer själv.
city=["Motala","Borensberg","Vadstena","Klockrike","Tjällmo"]
city.append(input("Lägg till stad: "))
print(city)
city.remove(input("Ta bort stad: "))
print(city)
print(len(city))
print("Första staden: "+city[0]+ " Sista staden: "+city[-1])
city.append(input("Lägg till tre städer: "))
print(city)
