import smtplib
import random
import datetime as dt

mail = "karumanchi304@gmail.com"
password = ""


with open("quotes.txt", 'r', encoding="utf8") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

message = "Subject:Monday Quote\n\n" + quote


now = dt.datetime.now()
year = now.year
month = now.month   
day_of_week = now.weekday()
if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # make the connection secure, encrypted
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail, 
            to_addrs="karumanchi304@yahoo.com", 
            msg=message.encode('utf-8')
    )   # \n\n is used to separate the subject from the body of the email



   