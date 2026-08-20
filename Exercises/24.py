#Uppgift: Utgå från en lista med kurser som innehåller course, points och rate.
#Krav: - Sortera kurser efter HP - Sortera kurser efter studietakt - Skriv ut resultaten
#Challenge: Sortera från högst till lägst med reverse=True.
#Extra: Använd lambda som key.
def sort_by_hp(courses):
    return sorted(courses, key=lambda p:p["hp"])

def sort_by_rate(courses):
    return sorted(courses, key=lambda p:p["rate"])

def sort_by_name(courses):
     return sorted(courses, key=lambda p:p["name"],reverse=True)

courses=[{"name":"kurs a","hp":3,"rate":20},
         {"name":"kurs b","hp":7.5,"rate":40},
         {"name":"kurs c","hp":4,"rate":30}]

print(sort_by_hp(courses))
print(sort_by_rate(courses))
print(sort_by_name(courses))
