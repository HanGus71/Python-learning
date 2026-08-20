days=['Mon','Sun','Wed','Tue']
weekends=['Sat','Sun']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')
print("Klart")