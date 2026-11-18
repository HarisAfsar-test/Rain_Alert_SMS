import requests
#CONSTANTS
MY_LAT=33.640091
MY_LON=73.066293
API_KEY="52eb61189c4b96e5b3ca808101641425"
API_KEY_2= 'txb_6pQteiktRa95NdWlHg9cT7daFMGhvYkm'
DEVICE_ID="6afd954b5b9635c5dd3cc774"
NUMBER= "+923355785260"
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

