#Förklara varför följande är fel och rätta koden
#Krav: -Identifiera felet utan att köra koden först -Förklara varför funktionen skrivs över -Skriv en korrekt version
#def clean_name(name):
    #cleaned = name.strip()
    #return cleaned

#clean_name = input("Name: ")
#print(clean_name("Maria"))
#paremeter name ska tilldelas värde inte clean_name
def clean_name(name):
    cleaned = name.strip()
    return cleaned

name = input("Name: ")
print(clean_name(name))