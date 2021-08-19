def main():
     email_name = {}
     email = input("Please enter your email address: ")
     while email != "":
         name = get_email_name(email)
         verify = input("Is your name {}? (Y/n) ".format(name))
         if verify.upper() != "Y" and verify != "":
             name = input("Name: ")
         email_name[email] = name
         email = input("Email: ")
 
     for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_email_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
