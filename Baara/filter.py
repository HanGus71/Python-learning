letters=['a','','b',None,'c']
#print(list(filter(bool, letters)))

items=['sql','123','python','42']
print(list(filter(str.isalpha,items)))