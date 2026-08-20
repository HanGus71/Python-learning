scores =[80,50,60,75]
total=0
for score in scores:
    total+=score
    print("Current Total:", total)
print("Final Total:",total)

files=[' Report.csv', 'DATA.csv', ' final.TXT']
for file in files:
    file=file.strip().lower().replace(".txt",".csv")
    print(f"Processing {file}")