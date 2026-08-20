#Uppgift: Låt användaren skriva in ett ord. Skriv ut första tecknet, sista tecknet, de tre första tecknen och de två sista tecknen.
#Challenge: Kontrollera om ordet är ett palindrom.
word=input("Skriv ett ord: ")
print("Första: "+word[0] +
      " Sista: "+word[-1]+
      " Första tre: "+word[:3]+
      " Sista två: "+word[-2:])
word_rev=word[::-1]
print(word_rev)
if word==word_rev:
    print("Det är ett palindrom!")