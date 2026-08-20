def is_valid_pwd(password):
    return len(password)>=8

print(is_valid_pwd("12345678"))

def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("jdjdj@jjd.com"))
