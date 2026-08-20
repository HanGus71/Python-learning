letters=['a','b','c']
print(list(map(str.upper,letters)))

numbers=['1','2','3']
print(list(map(int, numbers)))

names=[' Hans ','Lennart ',' Folke']
print(list(map(str.strip,names)))