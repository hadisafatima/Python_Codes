# This program takes emails from user to validate them and store all the emails in a dictionary
# That dictionary has two keys "valid" and "invalid", value for "valid" key is a list if valid email(s) and that of 
# "invlaid" key is a list of invalid email(s) 


import time
import re

class Email_validation :
    def __init__(self, mails):
        self.emails = mails
        self.mail_regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.results = {"valid": [], "invalid": []}


    def validating(self) :
        for _ in range(5) : # for this outer loop "_" is used instead of any variable bcuz that variable won't be used anywhere, therefore, in such cases we can always use "_"  
            dots = ". . . . . "
            for i in dots :
                print(i, end = "", flush = "True")
                time.sleep(0.1)

            print("\r" + "" * len(dots), end="") 

        for m in self.emails :
            m = m.strip()
            if re.match(self.mail_regex, m) :
                self.results["valid"].append(m)
            else :
                self.results["invalid"].append(m)

                
        print("\n\n\t\t\t\t\t\t-Emails Validation Completed-\n\n")

    def print_emails(self) :

        if len(self.results["valid"]) > 0 :
            print("\n\nValid Emails : ")
            for id , email in enumerate(self.results["valid"], 1) :
                print(f"{id}. {email}")
        elif len(self.results["valid"]) == 0:
            print("\nNo valid E-mails")


        if len(self.results["invalid"]) > 0 :
            print("\n\nInvalid Emails : ")
            for id, email in enumerate(self.results["invalid"], 1) :
                print(f"{id}. {email}")
        elif len(self.invalid) == 0:
            print("\nNo In-valid E-mails")




emails = input("Enter E-mails that you want to validate : (E-mails should be comma separated)\n")
emails_list = emails.split(",")
email_validation = Email_validation(emails_list)
email_validation.validating()
email_validation.print_emails()