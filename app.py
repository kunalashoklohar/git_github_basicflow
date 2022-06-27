# 1. read availibilty.txt file and extract name,email,and availability string and will create a datastructure /

# 2.from that data structure ,calculate most efficeint timming

# 3.email this timmimng to everyone

import smtplib

def read_availabilty(file_name="C:\Projects\demo_venv\availability.txt"):
    name_timming = {}
    name_emailid = {}
    return name_timming, name_emailid



def efficient_timming(name_timming:dict):
    timming = ""
    return timming

name_emailid = {"kunal":"kunal@gmail.com", "shubham":"shubham@gmail.com"}    


def read_password(file = "password.txt"):
    return "password"

def sent_email(message:str, senders_credentias:dict, email_ids:list):
    # Python code to illustrate Sending mail from 
    # your Gmail account
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(senders_credentias['email_id'], senders_credentias['password'])
    
    # message to be sent
    
    for email_id in email_ids:
        # sending the mail
        s.sendmail(senders_credentias['email_id'], email_id, message)
    
    # terminating the session
    s.quit()

