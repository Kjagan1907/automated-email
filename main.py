import smtplib
import random
import datetime as dt
import pandas as pd

mail = "karumanchi304@gmail.com"
password = ""

now = dt.datetime.now()
year = now.year
month = now.month   
day_of_week = now.weekday()

today = (month, now.day)

with open("birthdays.csv", 'r') as file:
    df = pd.read_csv(file)
    dictionary = df.to_dict()
    dictionary = {(dictionary["month"][i], dictionary["day"][i]): dictionary["name"][i] for i in range(len(dictionary["month"]))}
    if today in dictionary:
        name = dictionary[today]
        with open(f"letter_{random.randint(1,3)}.txt", 'r') as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", name)
        message = f"Subject:Happy Birthday\n\n{letter}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # make the connection secure, encrypted
            connection.login(user=mail, password=password)
            connection.sendmail(
                from_addr=mail, 
                to_addrs="karumanchi304@yahoo.com", 
                msg=message.encode('utf-8')
        )   # \n\n is used to separate the subject from the body of the email
        



   