import random
import smtplib
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
        print(data)

my_email = "test@gmail.com"
password = "password"

# Définir le port et augmenter le délai d'attente
smtp_port = 587
timeout = 30

try:
    with smtplib.SMTP("smtp.gmail.com", port=smtp_port, timeout=timeout) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
