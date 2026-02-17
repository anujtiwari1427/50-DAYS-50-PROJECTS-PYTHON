flow_rate = float(input("Enter water flow rate (L/min):  "))

if flow_rate > 25:
    print("🚨 Possible Water Leakage Detected!")
else:
    print("✅ Flow Normal")