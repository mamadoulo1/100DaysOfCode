import datetime as dt
import random
import smtplib

import pandas as pd

##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        text = letter_file.read()
        text = text.replace("[NAME]", birthday_person['name'])
        print(text)



# 4. Send the letter generated in step 3 to that person's email address.
my_email = "test@gmail.com"
password = "password"

smtp_port = 587
timeout = 30
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
try:
    with smtplib.SMTP("smtp.gmail.com", port=smtp_port, timeout=timeout) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@gmail.com",
            msg=f"Subject:Happy Birthday\n\n{text}"
        )
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")


