import smtplib
my_email = "adewalep096@gmail.com"
password = "emperor11@"

try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is the port number for TLS
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="adewalep097@gmail.com", msg="Subject:This is the practical sample")
    connection.quit()  # Use quit() instead of close()
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your email and password.")
except smtplib.SMTPException as e:
    print("Error sending email:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

#import Time
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=2, day=1, hour=4)
print(date_of_birth)

