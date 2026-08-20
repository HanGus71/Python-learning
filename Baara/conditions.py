score=40
project=True
if score >=90 and project:
    print("A+")
elif score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60 or project:
    print("D")
else:
    print("F")

score=81
if score >=90:
    print("A")
else:
    print("F")
print("A" if score >=90 else "B" if score >=80 else "F")
country="Sverige"
match country:
    case "Sverige":
        print("SE")
    case "Norge":
        print("NO")