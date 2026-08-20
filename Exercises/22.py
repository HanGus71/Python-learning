#Uppgift: Skapa en lista med fem personer. Varje person ska vara en dictionary med name, age och city.
#Krav: - Loopa genom listan- Skriv ut namn och ålder- Skriv ut personer över 50- Beräkna medelåldern
#Challenge: Skapa `sort_people_by_age(people)` som returnerar en ny lista
#där personerna är sorterade efter ålder, från yngst till äldst.
def create_dic(persons,ages):
    people=[]
    for i in range(len(persons)):
        dic={
            "name":persons[i],
            "age":ages[i],
            "city":"Kode"
        }
        people.append(dic)
    return people

persons=["Hans","Peter","Tommy","Perra","Anna"]
ages=[55,60,45,52,50]

return_dic=create_dic(persons,ages)
print(return_dic)

def print_calc_age(persons):
    total_age=0
    count=0
    for p in persons:
        if p["age"]>50:
            print(p["name"],p["age"])
            total_age+=p["age"]
            count+=1
    print("Medelålder: ",round(total_age/count,1))

print_calc_age(return_dic)

def sort_people_by_age(people):
    return sorted(people, key=lambda p:p["age"])

sorted_people = sort_people_by_age(return_dic)

print(sorted_people)
        


