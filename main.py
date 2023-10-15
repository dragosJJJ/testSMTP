import smtplib,random

my_email = "testmail@gmail.com"
password = "testpassword"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password=password)
with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

connection.sendmail(
    from_addr=my_email,
    to_addrs="draxgamer12@gmail.com",
    msg=f"Subject:Hello\n\n{quote}"
)
connection.close()