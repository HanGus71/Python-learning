def clean_and_split_email(email):
    cl_email=email.strip().lower()
    username, domain = cl_email.split("@")
    return {"username":username,"domain":domain}

print(clean_and_split_email("hg@gmail.com)"))