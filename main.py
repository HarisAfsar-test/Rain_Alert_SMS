import requests
import os
#CONSTANTS
MY_LAT=os.environ.get("MY_LAT")
MY_LON=os.environ.get("MY_LON")
API_KEY=os.environ.get("API_KEY")
API_KEY_2=os.environ.get("API_KEY_2")
DEVICE_ID=os.environ.get("DEVICE_ID")
NUMBER=os.environ.get("NUMBER")
parameters={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":API_KEY,
    "cnt":4,
}
data=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
data.raise_for_status()
data=data.json()
weather_data=data["list"]
will_rain=True

for hour in weather_data:
    condition_check=hour["weather"][0]["id"]
    if int(condition_check)<700:
      will_rain=False
if will_rain:
    print("Please bring umbrella !")
else:
     print("Please bring umbrella  not!")
if will_rain:
    res = requests.post(
        'https://api.textbee.dev/api/v1/gateway/send-sms',
        headers={'x-api-key': API_KEY_2},
        json={
            'deviceId': DEVICE_ID,
            'recipients': [NUMBER],
            'message': 'Please bring umbrella!\nThere are chances of rain',
        },
    )

