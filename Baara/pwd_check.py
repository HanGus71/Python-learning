email="A"
pwd="51A!!!!bc"
valid=True
if pwd == "":
    print("Pwd tomt")
    valid=False
if len(pwd)<8:
    print("Pwd har mindre än 8 tecken")
    valid=False
if sum(tecken.isupper() for tecken in pwd)<1:
    print("Saknar uppercase")
    valid=False
if sum(tecken.islower() for tecken in pwd)<1:
    print("Saknar lowercase")
    valid=False
if pwd == email:
    print("Samma pwd som e-mail")
    valid=False
if pwd.count(" ") > 0:
    print("Får ej innehålla blanksteg")
    valid=False
if not (pwd[0].isalnum() and pwd[-1].isalnum()):
    print("Måste starta och sluta med siffra eller bokstav")
    valid=False
if valid!=False:
    print("E-mail ok")