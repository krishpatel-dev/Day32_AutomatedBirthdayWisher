import datetime as dt
import smtplib
import random

MY_EMAIL = "dumphere0001@gmail.com"
SENDING_EMAIL = "dumphere0002@gmail.com"
MY_PASSWORD = "pbamackhxcbgnxik"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=SENDING_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )