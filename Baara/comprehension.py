domains=['www.glg.com',
'openai.com',
'localhost',
'WWW.HANSG.COM']

cleaned=[
    d.lower().replace('www.','')
    for d in domains
    if '.' in d
]
print(cleaned)