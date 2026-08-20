#Be användaren ange två heltal och skriv ut summa, differens, produkt, kvot, heltalsdivision och rest.
#Challenge: Använd `%` för att avgöra om det första talet är jämnt eller udda.
heltal=input("Ange två heltal, separera med komma: ")
a,b=heltal.split(",")
a=int(a)
b=int(b)
print("Summan är: ",a+b)
if a % 2!=0:
   print("Första talet är ojämnt!")
else:
   print("Första talet är jämnt!")