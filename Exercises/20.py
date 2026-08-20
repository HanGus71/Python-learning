#Uppgift: Bygg ett litet program för en person som läser kurser. Programmet ska fråga efter namn, kurs, HP och studietakt. Beräkna studietimmar per vecka baserat på 40 timmar vid 100 % och visa en tydlig sammanställning.
#Challenge: Låt användaren lägga till flera kurser och räkna ut total studietid per vecka.
def calc_study_hours(rate):
    return rate*40/100
    

courses=[]

while True:
    name=input("Ange namn: ")
    course=input("Ange kurs: ")
    points=int(input("Ange högskolepoäng, hp: "))
    rate=int(input("Ange studietakt i procent: "))
    hours=calc_study_hours(rate)

    course_info = {
    "name": name,
    "course": course,
    "points": points,
    "rate": rate,
    "hours": calc_study_hours(rate)
}

    courses.append(course_info)


    new_course=input("Vill du registrera fler kurser, ange ja: ")

    if new_course != "ja":
        break
    
print("\n--- Kurssammanställning ---")

for course in courses:
    print(
        f'{course["course"]}: '
        f'{course["points"]} HP | '
        f'{course["rate"]}% | '
        f'{course["hours"]:.1f} timmar/vecka'
    )

total_hours=0
for course in courses:
    total_hours+=course["hours"]
print("Total studietid i veckan: ",total_hours," timmar")
