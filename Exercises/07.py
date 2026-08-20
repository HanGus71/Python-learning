#Uppgift: Be användaren skriva in rätt lösenord. Fortsätt fråga tills lösenordet är rätt
#Challenge: Tillåt maximalt tre försök.
password=("Hejpådig")
def check_password(pwd):
    attempts=0
    while password !=pwd:
        attempts+=1
        if attempts==3:
            print("Tre försök förbrukade!")
            return
        pwd=input("Skriv in rätt lösenord:")
    print("Rätt lösenord")
check_password(input("Ange lösenord: "))

