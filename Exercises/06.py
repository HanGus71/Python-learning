#Uppgift: Skriv ut talen 1–20 och sedan bara de jämna talen.
#Beräkna summan av talen 1–100 utan sum().
print(list(range(1, 21)))
for n in range(1,21):
    if n % 2 ==0:
        print(n)

t=0
for n in range(1,101):
    t=t+n
print(t)