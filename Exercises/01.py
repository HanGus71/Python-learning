#Be användaren ange namn, ålder och stad. Spara varje svar i en egen variabel och skriv sedan ut en sammanhängande mening.
### Challenge: Beräkna hur gammal personen är om 10 år.
name=input("Ange namn: ")
age=int(input("Ange ålder: "))
city=input("Ange stad: ")
age_10=(age+10)
print(name +" "+str(age)+" "+city+" Ålder om 10 år: "+str(age_10))