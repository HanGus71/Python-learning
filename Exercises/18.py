#Uppgift: Skapa en dictionary med fem personer och deras ålder. Loopa igenom dictionaryn och skriv ut alla personer som är 50 år eller äldre.
#Challenge: Beräkna medelåldern.
person_dic={"Hans":55,"Anna":50,"Tommy":45,"Annelie":43,"Peter":60}
#print(len(person_dic))
sum_over_50=0
sum_all=0
count_over_50=0
for name, age in person_dic.items():
    if age >=50:
        count_over_50+=1
        print(name,age)
        sum_over_50+=age
    sum_all+=age
print("Medelålder över 50: ",sum_over_50/count_over_50)
print("Medelålder för alla: ",sum_all/len(person_dic))