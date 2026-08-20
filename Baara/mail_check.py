mail="hans@gmail.com"
if mail !="":
    if mail.find(".") and mail.find("@"):
        if mail.count("@") == 1:
            if mail.endswith(".com") or mail.endswith(".org") or mail.endswith(".net"):
                if len(mail)<=254:
                   if mail[0].isalpha() or mail[0].isdigit():
                        if mail[-1].isalpha() or mail[-1].isdigit():
                            print("E-mail ok")
          