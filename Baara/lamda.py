multiple=lambda x: x*2
print(multiple(10))

add=lambda x, y: x+y
print(add(1,2))

check=lambda i: i in "python"
print(check('x'))

prices=['$12.50','$10.40','$100.00']
print(list(map(lambda p: float(p.replace('$','')),prices)))

students = [['Hans',60],
            ['Lennart', 90],
            ['Folke',95]]
print(list(filter(lambda row:row[1]>70,students)))
print(students[0][1]>70)