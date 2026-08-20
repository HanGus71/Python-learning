#Uppgift: Skapa calculate_hours(study_rate) där 100 % motsvarar 40 timmar/vecka. Använd en lista med studietakter och skriv ut timmarna för varje takt.
#Challenge: Skapa en dictionary där studietakten är key och timmarna är value.
def calculate_hours(study_rate):
    return round(study_rate*0.01*40,1)

#rate_dic={}
for r in range(1,101):
    rate_dic[r]=calculate_hours(r)
    #print(str(r) + "% -> "+str(round(hour,1)))
print(rate_dic)



