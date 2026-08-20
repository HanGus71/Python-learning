#Projekt – Kursprogram: Bygg ett program för en person som läser kurser.
#Programmet ska kunna: - Lägga till kurs
#- Beräkna timmar per vecka
#- Visa alla kurser
#- Beräkna total studietid
#- Söka kurs
#- Ändra studietakt
#- Ta bort kurs
#Föreslagna funktioner: add_course(), calc_study_hours(), show_courses(), calc_total_hours(), find_course(), remove_course(),update_rate(), save_courses(), load_courses(), run_menu()
#Challenge: Skapa en meny med alternativ för att lägga till, visa, söka, ändra, ta bort och avsluta.
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "courses.json")


def add_course(courses):
    while True:
        name=input("Ange namn: ")
        course=input("Ange kurs: ")
        points=float(input("Ange högskolepoäng, hp: "))
        rate=int(input("Ange studietakt i procent: "))
                       
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
    

def calc_study_hours(rate):
    return rate*40/100

def show_courses(courses):
    print("\n",
        "-"*25,"Kurssammanställning","-"*25,
          )
    print(f'{"Namn":<20}{"Kurs":<25}{"HP":>6}{"Takt":>7}{"Tid/vecka":>13}')
    print("-" * 71)

    for course in courses:
        print( 
            f'{course["name"]:<20}'
            f'{course["course"]:<25}'
            f'{course["points"]:>5.1f} '
            f'{course["rate"]:>6}% '
            f'{course["hours"]:>10.1f} h'
        )
    print()
    print("Total studietid i veckan: ",calc_total_hours(courses)," timmar")
    print()

def calc_total_hours(courses):
    total_hours=0
    for course in courses:
        total_hours+=course["hours"]
    return total_hours

def find_course(courses):
    found=False
    name_return=input("Ange sökt kurs: ")
    for c in courses:
            if name_return ==c["course"]:
                print("Kursen är registrerad: ",c["course"])
                found=True
    if not found:
            print("Kursen är inte registrerad!")

def update_rate(courses):
    found=False
    name_change=input("Ange kurs du vill ändra studietakt på: ")
    for c in courses:
        if name_change == c["course"]:
            c["rate"] = int(input(f"{c['course'].capitalize()} - ändra studietakt: "))
            c["hours"]=calc_study_hours(c["rate"])
            found = True
    if not found:
        print("Kursen saknas!")

def remove_course(courses):
    found=False
    name_remove=input("Ange kurs du vill ta bort: ")
    for c in courses:
        if name_remove ==c["course"]:
            courses.remove(c)
            print("Kursen togs bort!")
            found=True
            break
    if not found:
        print("Kursen saknas!")
        

def save_courses(courses):
    with open(FILE_PATH, "w") as file:
        json.dump(courses, file, indent=4)

def load_courses():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def run_menu():
    courses = load_courses()

    while True:

        print("-"*10,"Meny","-"*10)
        print()
        print("1 Lägga till kurs")
        print("2 Visa alla kurser")
        print("3 Söka kurs")
        print("4 Ändra studietakt")
        print("5 Ta bort kurs")
        print("6 Avsluta programmet")
        print()

        meny_val = input("Ange siffra för ditt val: ")


        if meny_val == "1":
            add_course(courses)

        elif meny_val == "2":
            show_courses(courses)

        elif meny_val == "3":
            find_course(courses)

        elif meny_val == "4":
            update_rate(courses)

        elif meny_val == "5":
            remove_course(courses)

        elif meny_val == "6":
            save_courses(courses)
            break


run_menu()
