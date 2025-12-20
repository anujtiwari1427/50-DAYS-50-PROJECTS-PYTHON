aqi = int(input("Enter AQI value: "))

if aqi > 300:
    print("🚨 Severe Pollution – Stay Indoors!")
elif aqi > 150:
    print("⚠️ Unhealthy Air")
else:
    print("✅ Air Quality Good")
