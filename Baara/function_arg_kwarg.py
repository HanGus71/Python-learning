def total(*args):
    print(sum(args))

total(1,2,3,4,5,10)

def create_user(**kwargs):
    print(kwargs)

create_user(first_name="Hans",
            last_name="Gustafsson",
            age=55,
            country="Sweden")