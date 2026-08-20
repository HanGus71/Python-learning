i=0
while True:
    answer=input("Do you agree? (yes/no): ")
                #print("3 Strikes, You are out")
    i=i+1
    if i==3:
           print("3 Strikes, You are out")
           break
    if answer == "yes":
             print("Glad we are on same page")
             break
