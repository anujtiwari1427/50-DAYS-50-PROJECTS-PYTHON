import requests
import os

def telegram_bot_send_text(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chatID = os.environ.get("BOT_CHATID")
    send_text = "https://api.telegram.org/bot"+bot_token+ '/sendMessage?chat_id='+ bot_chatID \
                + '&parse_mode=Markdown&text=' + bot_message
    
    bot_response = requests.get(send_text)
    return bot_response.json()

api_key = os.environ.get("API_KEY")

parameters = {
    "lat": 43.6532225,
    "lon": -79.383186,
    "exclude": "current,minutely,daily",
    "appid":api_key,
}
url ="https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&hourly=temperature_2m,weathercode"
response = requests.get(url)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour in range(12):
    weather_code = weather_data["hourly"]["weathercode"][hour]

    if weather_code < 70:
        will_rain = True

    if will_rain:
        message = "🌧 It's going https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true to rain today, bring an umbrella with you."
        telegram_bot_send_text(message)