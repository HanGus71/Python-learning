letters=['a','b','c']
numbers=[1,2,3]
#new_list=[]
#for l in list:
#    new_list.append(l.upper())
#    print(new_list)
#print(list(enumerate(letters)))
#for index,value in enumerate(letters):
 #   print(index,value)
#for l in reversed(letters):
 #   print(l)
for l, n in zip(letters,numbers):
    print(l,n)
#print(list(zip(letters,numbers)))