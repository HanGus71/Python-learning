# Uppgift Skapa `clean_name(name, case_rule)` som tar bort inledande/avslutande mellanslag och därefter gör texten lowercase eller uppercase beroende på `case_rule'
#Challenge: Om case_rule är något annat: lämna namnet oförändrat.
case_rule="lower"
def clean_name(name):
        if case_rule == "lower":
            name=name.lower()
        return name
name=input("Namn: ")
print(clean_name(name))