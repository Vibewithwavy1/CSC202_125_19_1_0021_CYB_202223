import time

import requests
from datetime import datetime
import smtplib

MY_EMAIL = "adewalep096@gmail.com"
MY_PASSWORD = "emperor11@"
MY_LAT = 51.507351
MY_LONG = -0.127758

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #your position is within +5 and -5 degrees of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response =  requests.get("https://api.sunrise-sunset.org/json", param = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login((MY_EMAIL,MY_PASSWORD))
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            MSG = "Subject:Look Up \n\n The ISS is above you in the sky "
        )

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code != 200:
#     raise Exception("Bad response from ISS")
# elif response.status_code == 404:
#     raise Exception("You are not authorised to access this data")
# else:
#     raise Exception("You are good to go")

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

#response code, http