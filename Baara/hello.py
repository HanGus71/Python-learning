#1
username="a"
age=24
print(username != "" and age>18)
#2
password="5hd12 873"
#print(password.find(" "))
print(len(password)>=8 and password.find(" ") == -1)
#3
mail="hg@gmail.com"
print(mail != "" and mail.find("@")>-1 and mail.endswith(".com"))
#4
username="hsdsss"
print(username.isalpha() and len(username)>5 and username is not None)
#5
user="admin"
banned="no"
mail_verified="yes"
print(user in["admin","moderator"] and (banned == "no" or mail_verified == "yes"))