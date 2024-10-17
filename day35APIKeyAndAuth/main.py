import requests
from twilio.rest import Client

params = {
    "appid": "id",
    "lat": 45.833618,
    "lon": 1.261105,
    "cnt": 4
}

account_sid = ''
auth_token = ''

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()

data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18643875420",
        to="+33626582134",
    )
print(message.status)