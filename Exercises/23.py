#Uppgift: Utgå från en lista med kurser som innehåller course, points och rate. Sök efter en kurs med ett visst namn och skriv ut dess HP.
#Challenge: Ändra studietakten och hantera fallet då kursen saknas.
#Extra:Skapa funktionerna find_course() och update_rate().

def find_course(courses,name_return):
    found=False

    for c in courses:
        if name_return ==c["name"]:
            print("Antal HP: ",c["hp"])
            found=True
    if not found:
        print("Kursen saknas!")

def update_rate(courses,name_change):
    found=False

    for c in courses:
        if name_change == c["name"]:
            c["rate"] = int(input(f"{c['name'].capitalize()} - ändra studietakt: "))
            found = True
    if not found:
        print("Kursen saknas!")

courses=[{"name":"kurs a","hp":3,"rate":20},
         {"name":"kurs b","hp":7.5,"rate":33},
         {"name":"kurs c","hp":4,"rate":30}]

name_return=input("Ange kurs (HP returneras): ")
find_course(courses,name_return)

name_change=input("Ange kurs du vill ändra studietakt på: ")
update_rate(courses,name_change)

print(courses)