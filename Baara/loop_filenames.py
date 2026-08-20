file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
    ]
for files in file_list:
    if file_list.count(files)>1:
        print("Duplicate found")
        break
else:
    print("All files are unique")