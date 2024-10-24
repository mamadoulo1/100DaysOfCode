import requests

MY_LAT = 48.856613
MY_LONG = 2.352222

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]