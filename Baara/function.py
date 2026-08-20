print ("Start")
def greet():
    print("Hello")
greet()
greet()
print("End!")

import math
print(len("Python"))

number=4.2
print(math.floor(number))

case_rule = "upper"

def clean_name(name):
    cleaned=name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
    elif case_rule == "upper":
        cleaned = cleaned.upper()
    print("Cleaned:",cleaned)

clean_name(input("Name: "))

case_rule = "lower"

def clean_name(first_name,last_name,country="n/a"):
    cleaned=first_name.strip() +" "+ last_name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
    elif case_rule == "upper":
        cleaned = cleaned.upper()
    print("Cleaned:",cleaned," "+country)

clean_name(first_name=input("Förnamn: "),last_name=input("Efternamn: "),country=input("Land: "))