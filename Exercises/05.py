#Uppgift: Be användaren ange en temperatur och klassificera den: under 0 Frost, 0–9 Kallt, 10–19 Svalt, 20–29 Behagligt, 30+ Varmt.
#Challenge: Gör programmet med en funktion classify_temperature(temp) som returnerar texten.
def classify_temperature(temp):
    if temp < 0:return "Frost"
    elif temp < 10:return "Kallt"
    elif temp < 20:return "Svalt"
    elif temp <= 30:return "Behagligt"
    else: return "Varmt"
temp=int(input("Ange temp: "))
print(classify_temperature(temp))
