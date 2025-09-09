import smtplib

#dump1pass: pbamackhxcbgnxik
#dump2pass: bsejygtlzyowvokg


my_email = "dumphere0002@gmail.com"
password = "bsejygtlzyowvokg"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dumphere0001@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )
