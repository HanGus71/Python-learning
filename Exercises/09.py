#Uppgift: Skapa en lista med talen 1–20 och skapa sedan en ny lista med kvadraten av varje tal.
#Challenge: Skapa en lista med endast jämna tal och en lista med endast tal större än 10.
#Extra: skriv först lösningen med for och därefter med list comprehension.
numbers=[n for n in range (1,21)]
print(numbers)
square=[s*s for s in range (1,21)]
print(square)
even=[e for e in range(1,21) if (e%2 == 0)]
print(even)
large=[l for l in range(1,21) if l>10]
print(large)
large_for=[]
for l in range(1,21):
    if l >10:
        large_for.append(l)
print(large_for)

large_numbers=[n for n in numbers if n>10]
print(large_numbers)